days_loop = int(input())

doctors = 7
examined = 0
transferred = 0

for i in range(1, days_loop+1):
    patients = int(input())
    if (i % 3 == 0) and transferred > examined:
        doctors = doctors + 1

    if patients > doctors:
        transferred = transferred + (patients - doctors)
        examined = examined + doctors
    elif patients <= doctors:
        examined = examined + patients



print(f"Treated patients: {examined}.")
print(f"Untreated patients: {transferred}.")
