from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Group.objects.all()
    )

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        groups = validated_data.pop('groups', [])
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        user.groups.set(groups)
        return user

    def update(self, instance, validated_data):
        groups = validated_data.pop('groups', None)
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()

        if groups is not None:
            instance.groups.set(groups)

        return instance



class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = '__all__'


class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'cardholder_name', 'card_number', 'expiry_date', 'cvv']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ParkingNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingNotification
        fields = '__all__'


class FamilyCommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyCommunity
        fields = '__all__'


class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = '__all__'


class FamilyInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyInvitation
        fields = '__all__'


class FavoriteGarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteGarage
        fields = '__all__'


class ParkingSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSubscription
        fields = '__all__'


class ParkingSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSensor
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    license_plate = serializers.CharField(write_only=True)
    car_model = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', 'national_id',
            'password', 'profile_picture', 'gender', 'license_id',
            'license_plate', 'car_model'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        license_plate = validated_data.pop('license_plate')
        car_model = validated_data.pop('car_model')

        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        try:
            Vehicle.objects.create(
                user=user,
                license_plate=license_plate,
                car_model=car_model
            )
        except IntegrityError as e:
            print(f"Vehicle creation error: {e}")
            # Optional: you could delete the user or raise a validation error
            user.delete()
            raise serializers.ValidationError("Vehicle already exists or data is invalid.")

        return user

from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)  # ✅ Email-based auth

            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is deactivated.")
                return user
            else:
                raise serializers.ValidationError("Invalid email or password.")
        else:
            raise serializers.ValidationError("Both email and password are required.")


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, min_length=8)

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email not found.")
        return value

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data

    def save(self):
        email = self.validated_data['email']
        new_password = self.validated_data['new_password']
        user = User.objects.get(email=email)
        user.set_password(new_password)
        user.save()
        return user


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = '__all__'
