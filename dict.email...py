sample_api_response = {
    "status": "success",
    "data": {
        "users": [
            {
                "id": 12345,
                "name": "Gauri Dangi",
                "email": "gauri.dangi@example.com",
                "password": "MyPassword123"
            },
            {
                "id": 12346,
                "name": "Sita Rai",
                "email": "sita.rai@example.com",
                "password": "SecurePass456"
            },
            {
                "id": 12347,
                "name": "Rajesh Shrestha",
                "email": "rajesh.shrestha@example.com",
                "password": "Rajesh123!"
            }
        ]
    }
}
# sample_api_response[1]["data"]["user"]
# rajeshN = sample_api_response["data"]["users"][2]["name"]
# print(rajeshN)
# for userid in range(3):
users = sample_api_response["data"]["users"]
userid = int(input("Enter your id."))

for user in users:
    if (userid==user["id"]):
        print(f"Your name is {user["name"]}")
        
