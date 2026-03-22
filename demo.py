def nexa_os_demo(user_input):
    print(f"User Intent: {user_input}")
    print("→ Understanding intent...")
    print("→ Planning tasks...")
    print("→ Executing actions...")

    if "meeting" in user_input:
        print("✔ Calendar event created")
        print("✔ Reminder set")
        print("✔ Notification scheduled")
    else:
        print("✔ Task executed")

# Test
nexa_os_demo("Schedule meeting tomorrow")
