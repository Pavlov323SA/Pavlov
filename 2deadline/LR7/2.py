def build_user_profile(user_id: int, **user_info) -> dict:
    profile = {"user_id": user_id}
    for key, value in user_info.items():
        profile[key] = value
    return profile

profile = build_user_profile(101, name="Анна", status="online", email="anna@example.com")
print(profile)