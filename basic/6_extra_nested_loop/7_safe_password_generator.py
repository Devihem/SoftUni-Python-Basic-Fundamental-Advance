a_last = int(input())
b_last = int(input())
max_passwords = int(input())
X_counter = 35
Y_counter = 64
pass_gen_counter = 0
password_end_flag = True

while password_end_flag:

    for a in range(1, a_last+1+1):
        if not password_end_flag:
            break
        if a > a_last:
            password_end_flag = False
            break
        for b in range(1, b_last+1):
            if pass_gen_counter >= max_passwords:
                password_end_flag = False
                break
            pass_gen_counter += 1
            print(f"{chr(X_counter)}{chr(Y_counter)}{a}{b}{chr(Y_counter)}{chr(X_counter)}", end="|")
            X_counter += 1
            Y_counter += 1
            if X_counter > 55:
                X_counter = 35
            if Y_counter > 96:
                Y_counter = 64
