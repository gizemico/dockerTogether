from db.db_manager import connect_collection

device_collection = connect_collection("device_dict")


def read_device(devicenumber):
    document = device_collection.find_one({"device_number": devicenumber})
    if document:  # meaning we have a device with that specific number
        print("Device number:", devicenumber)
        print("Device IP:", document.get("device_ip"))
        print("Device port number:", document.get("device_port"))
        print("Device username:", document.get("device_username"))
        print("Device password:", document.get("device_password"))
    else:
        print("There is no device with this specific device number.")

    print(" ")

    # TODO READ all devices function oluştur, hata mesajı yolla

def read_all_devices():
    for document in device_collection.find():
        print("Device number:", document.get("device_number"))
        print("Device IP:", document.get("device_ip"))
        print("Device port number:", document.get("device_port"))
        print("Device username:", document.get("device_username"))
        print("Device password:", document.get("device_password"),"\n")

def add_device(device):
    if not device_collection.find_one({"device_number": device.device_number}):

        new_document = vars(device)
        # TODO document obje çevirisini düzelt (bir daha device classını importlamam gerekti)
        device_collection.insert_one(new_document)
        print(
            "Device with the  device number ",
            device.device_number,
            " has been successfully added to the database!",
            sep="",
        )
    else:
        print("There is already a device with the device number:", device.device_number)


def delete_device(number):
    device_collection.delete_one({"device_number": number})
    print(
        "Device with the device number",
        number,
        "has been successfully deleted from the database!",
    )


def update_device(device_num):
    print(" ")
    document = device_collection.find_one({"device_number": device_num})
    if document:  # meaning we have a device with that specific number
        print(
            "Please enter the new device information. Enter 'none' if you want the information to stay the same.\n"
        )
        new_device_number = input("Please enter a new device number: ")
        update_fields = {}

        if new_device_number != "":
            update_fields["device_number"] = new_device_number

        new_ip = input("Please enter a new ip number: ")
        if new_ip != "":
            update_fields["device_ip"] = new_ip

        new_port = input("Please enter a new port number: ")
        if new_port != "":
            update_fields["device_port"] = new_port

        new_username = input("Please enter a new username: ")
        if new_username != "":
            update_fields["device_username"] = new_username

        new_password = input("Please enter a new password: ")
        if new_password != "":
            update_fields["device_password"] = new_password

        if update_fields:  # Check if any fields were updated
            device_collection.update_one(
                {"device_number": device_num}, {"$set": update_fields}
            )

        print("Device is successfully updated!\n")
    else:
        print("There is no device with the number ", device_num, ".\n", sep="")
