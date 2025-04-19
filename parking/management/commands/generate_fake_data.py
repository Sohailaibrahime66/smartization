# from faker import Faker
# from parking.models import *
# import random
# from django.utils import timezone
# from datetime import timedelta
#
# # Initialize Faker instance
# fake = Faker()
#
# # Generate Fake Users
# def generate_fake_users(num_users=10):
#     users = []
#     for _ in range(num_users):
#         first_name = fake.first_name()
#         last_name = fake.last_name()
#         email = fake.email()
#         phone_number = fake.phone_number()
#         national_id = fake.unique.random_number(digits=14)
#         password = fake.password()
#         DOB = fake.date_of_birth(minimum_age=18, maximum_age=80)
#         gender = random.choice(['Male', 'Female'])
#         nationality = random.choice(['EGY', 'USA', 'CAN', 'UK', 'IN', 'AU', 'DE', 'FR', 'OT'])
#         subscription_type = random.choice(['standard', 'VIP'])
#         license_id = fake.file_name(extension='jpg')  # Fake file name for license image
#
#         # Create user
#         user = User.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             phone_number=phone_number,
#             national_id=national_id,
#             password=password,
#             DOB=DOB,
#             gender=gender,
#             nationality=nationality,
#             subscription_type=subscription_type,
#             license_id=license_id,
#             Registration_Date=timezone.now()
#         )
#         users.append(user)
#     return users
#
# # Generate Fake Cards
# def generate_fake_cards(num_cards=10, users=None):
#     cards = []
#     if not users:
#         users = User.objects.all()
#     for _ in range(num_cards):
#         user = random.choice(users)
#         cardholder_name = f"{user.first_name} {user.last_name}"
#         card_number = fake.credit_card_number(card_type='mastercard')
#         expiry_date = fake.future_date(end_date="+5y", tzinfo=None)
#         cvv = fake.credit_card_security_code()
#
#         # Create card
#         card = Card.objects.create(
#             user=user,
#             cardholder_name=cardholder_name,
#             card_number=card_number,
#             expiry_date=expiry_date,
#             cvv=cvv
#         )
#         cards.append(card)
#     return cards
#
# # Generate Fake Transactions
# def generate_fake_transactions(num_transactions=10, cards=None, users=None):
#     transactions = []
#     if not users:
#         users = User.objects.all()
#     if not cards:
#         cards = Card.objects.all()
#
#     for _ in range(num_transactions):
#         user = random.choice(users)
#         card = random.choice(cards)
#         amount = random.uniform(10.0, 500.0)
#         transaction_type = random.choice(['charge', 'spend'])
#         payment_time = fake.date_time_this_year(before_now=True, after_now=False)
#
#         # Create transaction
#         transaction = Transaction.objects.create(
#             user=user,
#             amount=round(amount, 2),
#             payment_time=payment_time,
#             type=transaction_type,
#             card=card
#         )
#         transactions.append(transaction)
#     return transactions
#
# # Generate Fake Garages
# def generate_fake_garages(num_garages=10):
#     garages = []
#     for _ in range(num_garages):
#         name = fake.company()
#         location = fake.address()
#         total_capacity = random.randint(50, 200)
#         available_capacity = random.randint(10, total_capacity)
#         opening_hours = fake.time()
#         closing_hours = fake.time()
#         no_of_floors = str(random.randint(1, 5))
#         price_per_hour = str(random.randint(50, 200))
#         price_per_month = str(random.randint(500, 2000))
#         rating = str(random.uniform(1, 5))
#
#         garage = Garage.objects.create(
#             name=name,
#             location=location,
#             total_capacity=total_capacity,
#             available_capacity=available_capacity,
#             opening_hours=opening_hours,
#             closing_hours=closing_hours,
#             no_of_floors=no_of_floors,
#             price_per_hour=price_per_hour,
#             price_per_month=price_per_month,
#             rating=rating
#         )
#         garages.append(garage)
#     return garages
#
# # Generate Fake Parking Slots
# def generate_fake_parking_slots(num_slots=10, garages=None):
#     slots = []
#     if not garages:
#         garages = Garage.objects.all()
#     for _ in range(num_slots):
#         garage = random.choice(garages)
#         slot_number = fake.bothify(text='??###')
#         is_occupied = random.choice([True, False])
#         is_reserved = random.choice([True, False])
#
#         slot = ParkingSlot.objects.create(
#             garage=garage,
#             slot_number=slot_number,
#             is_occupied=is_occupied,
#             is_reserved=is_reserved
#         )
#         slots.append(slot)
#     return slots
#
# # Generate Fake Vehicles
# def generate_fake_vehicles(num_vehicles=10, users=None):
#     vehicles = []
#     if not users:
#         users = User.objects.all()
#     for _ in range(num_vehicles):
#         user = random.choice(users)
#         vehicle_type = random.choice(['Car', 'Bike', 'Truck'])
#         license_plate = fake.license_plate()
#         car_model = fake.word()
#         vehicle_color = fake.color_name()
#
#         vehicle = Vehicle.objects.create(
#             user=user,
#             vehicle_type=vehicle_type,
#             license_plate=license_plate,
#             car_model=car_model,
#             vehicle_color=vehicle_color
#         )
#         vehicles.append(vehicle)
#     return vehicles
#
# # Generate Fake Reservations
# def generate_fake_reservations(num_reservations=10, users=None, vehicles=None, parking_slots=None):
#     reservations = []
#     if not users:
#         users = User.objects.all()
#     if not vehicles:
#         vehicles = Vehicle.objects.all()
#     if not parking_slots:
#         parking_slots = ParkingSlot.objects.all()
#
#     for _ in range(num_reservations):
#         user = random.choice(users)
#         vehicle = random.choice(vehicles)
#         parking_slot = random.choice(parking_slots)
#         start_time = fake.date_this_year(before_today=True, after_today=False)
#         end_time = start_time + timedelta(hours=random.randint(1, 5))
#         status = random.choice(['Reserved', 'Cancelled', 'Pending'])
#
#         reservation = Reservation.objects.create(
#             user=user,
#             vehicle=vehicle,
#             parking_slot=parking_slot,
#             start_time=start_time,
#             end_time=end_time,
#             status=status
#         )
#         reservations.append(reservation)
#     return reservations
#
# # Generate Fake Messages
# def generate_fake_messages(num_messages=10):
#     messages = []
#     for _ in range(num_messages):
#         message_type = random.choice(['Reservation Reminder', 'Payment Reminder', 'General Alert'])
#         message = fake.text()
#
#         msg = Message.objects.create(
#             type=message_type,
#             message=message
#         )
#         messages.append(msg)
#     return messages
#
# # Generate Fake Parking Notifications
# def generate_fake_parking_notifications(num_notifications=10, users=None, messages=None):
#     notifications = []
#     if not users:
#         users = User.objects.all()
#     if not messages:
#         messages = Message.objects.all()
#
#     for _ in range(num_notifications):
#         user = random.choice(users)
#         message = random.choice(messages)
#         notification_time = fake.date_time_this_year(before_now=True, after_now=False)
#         read = random.choice([True, False])
#
#         notification = ParkingNotification.objects.create(
#             user=user,
#             message=message,
#             notification_time=notification_time,
#             read=read
#         )
#         notifications.append(notification)
#     return notifications
#
# # Generate Fake Family Communities
# def generate_fake_family_communities(num_communities=10, users=None):
#     families = []
#     if not users:
#         users = User.objects.all()
#     for _ in range(num_communities):
#         name = fake.company()
#         created_by = random.choice(users)
#
#         family = FamilyCommunity.objects.create(
#             name=name,
#             created_by=created_by
#         )
#         families.append(family)
#     return families
#
# # Generate Fake Family Members
# def generate_fake_family_members(num_members=10, families=None, users=None):
#     family_members = []
#     if not families:
#         families = FamilyCommunity.objects.all()
#     if not users:
#         users = User.objects.all()
#
#     for _ in range(num_members):
#         family = random.choice(families)
#         user = random.choice(users)
#         role = random.choice(['Admin', 'Member'])
#
#         family_member = FamilyMember.objects.create(
#             family=family,
#             user=user,
#             role=role
#         )
#         family_members.append(family_member)
#     return family_members
#
# # Generate Fake Family Invitations
# def generate_fake_family_invitations(num_invitations=10, families=None, users=None):
#     invitations = []
#     if not families:
#         families = FamilyCommunity.objects.all()
#     if not users:
#         users = User.objects.all()
#
#     for _ in range(num_invitations):
#         inviter = random.choice(users)
#         invitee = random.choice(users)
#         family = random.choice(families)
#         accepted = random.choice([True, False, None])
#
#         invitation = FamilyInvitation.objects.create(
#             inviter=inviter,
#             invitee=invitee,
#             family=family,
#             accepted=accepted
#         )
#         invitations.append(invitation)
#     return invitations
#
# # Generate Fake Favorite Garages
# def generate_fake_favorite_garages(num_favorites=10, users=None, garages=None):
#     favorites = []
#     if not users:
#         users = User.objects.all()
#     if not garages:
#         garages = Garage.objects.all()
#
#     for _ in range(num_favorites):
#         user = random.choice(users)
#         garage = random.choice(garages)
#
#         favorite = FavoriteGarage.objects.create(
#             user=user,
#             garage=garage
#         )
#         favorites.append(favorite)
#     return favorites
#
# # Generate Fake Parking Subscriptions
# def generate_fake_parking_subscriptions(num_subscriptions=10, users=None, parking_slots=None):
#     subscriptions = []
#     if not users:
#         users = User.objects.all()
#     if not parking_slots:
#         parking_slots = ParkingSlot.objects.all()
#
#     for _ in range(num_subscriptions):
#         user = random.choice(users)
#         parking_slot = random.choice(parking_slots)
#         start_date = fake.date_this_year(before_today=True, after_today=False)
#         end_date = start_date + timedelta(days=random.randint(30, 365))
#         subscription_type = random.choice(['Monthly', 'Yearly'])
#         active = random.choice([True, False])
#
#         subscription = ParkingSubscription.objects.create(
#             user=user,
#             parking_slot=parking_slot,
#             start_date=start_date,
#             end_date=end_date,
#             subscription_type=subscription_type,
#             active=active
#         )
#         subscriptions.append(subscription)
#     return subscriptions
#
# # Generate Fake Parking Sensors
# def generate_fake_parking_sensors(num_sensors=10, parking_slots=None):
#     sensors = []
#     if not parking_slots:
#         parking_slots = ParkingSlot.objects.all()
#
#     for _ in range(num_sensors):
#         parking_slot = random.choice(parking_slots)
#         sensor_status = random.choice(['Active', 'Inactive'])
#         last_maintenance = fake.date_this_year(before_today=True, after_today=False)
#
#         sensor = ParkingSensor.objects.create(
#             parking_slot=parking_slot,
#             sensor_status=sensor_status,
#             last_maintenance=last_maintenance
#         )
#         sensors.append(sensor)
#     return sensors
#
# # Run the data generation process
# def generate_fake_data():
#     print("Generating fake users...")
#     users = generate_fake_users(num_users=50)  # Generate 50 fake users
#     print(f"Generated {len(users)} fake users.")
#
#     print("Generating fake cards...")
#     cards = generate_fake_cards(num_cards=100, users=users)  # Generate 100 fake cards
#     print(f"Generated {len(cards)} fake cards.")
#
#     print("Generating fake transactions...")
#     transactions = generate_fake_transactions(num_transactions=200, cards=cards, users=users)  # Generate 200 fake transactions
#     print(f"Generated {len(transactions)} fake transactions.")
#
#     print("Generating fake garages...")
#     garages = generate_fake_garages(num_garages=10)  # Generate 10 fake garages
#     print(f"Generated {len(garages)} fake garages.")
#
#     print("Generating fake parking slots...")
#     parking_slots = generate_fake_parking_slots(num_slots=50, garages=garages)  # Generate 50 fake parking slots
#     print(f"Generated {len(parking_slots)} fake parking slots.")
#
#     print("Generating fake vehicles...")
#     vehicles = generate_fake_vehicles(num_vehicles=100, users=users)  # Generate 100 fake vehicles
#     print(f"Generated {len(vehicles)} fake vehicles.")
#
#     print("Generating fake reservations...")
#     reservations = generate_fake_reservations(num_reservations=50, users=users, vehicles=vehicles, parking_slots=parking_slots)  # Generate 50 fake reservations
#     print(f"Generated {len(reservations)} fake reservations.")
#
#     print("Generating fake messages...")
#     messages = generate_fake_messages(num_messages=50)  # Generate 50 fake messages
#     print(f"Generated {len(messages)} fake messages.")
#
#     print("Generating fake parking notifications...")
#     notifications = generate_fake_parking_notifications(num_notifications=50, users=users, messages=messages)  # Generate 50 fake notifications
#     print(f"Generated {len(notifications)} fake parking notifications.")
#
#     print("Generating fake family communities...")
#     families = generate_fake_family_communities(num_communities=10, users=users)  # Generate 10 fake family communities
#     print(f"Generated {len(families)} fake family communities.")
#
#     print("Generating fake family members...")
#     family_members = generate_fake_family_members(num_members=50, families=families, users=users)  # Generate 50 fake family members
#     print(f"Generated {len(family_members)} fake family members.")
#
#     print("Generating fake family invitations...")
#     family_invitations = generate_fake_family_invitations(num_invitations=50, families=families, users=users)  # Generate 50 fake family invitations
#     print(f"Generated {len(family_invitations)} fake family invitations.")
#
#     print("Generating fake favorite garages...")
#     favorite_garages = generate_fake_favorite_garages(num_favorites=50, users=users, garages=garages)  # Generate 50 fake favorite garages
#     print(f"Generated {len(favorite_garages)} fake favorite garages.")
#
#     print("Generating fake parking subscriptions...")
#     parking_subscriptions = generate_fake_parking_subscriptions(num_subscriptions=50, users=users, parking_slots=parking_slots)  # Generate 50 fake parking subscriptions
#     print(f"Generated {len(parking_subscriptions)} fake parking subscriptions.")
#
#     print("Generating fake parking sensors...")
#     parking_sensors = generate_fake_parking_sensors(num_sensors=50, parking_slots=parking_slots)  # Generate 50 fake parking sensors
#     print(f"Generated {len(parking_sensors)} fake parking sensors.")
#
# # Call the function to generate data
# if __name__ == "__main__":
#     generate_fake_data()
