# write your code here
m_op = ["+", "-", "/", "*"]
condition_1 = False
memory = 0


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + " ... lazy"
    if (v1 == "1" or v2 == "1") and v3 == "*":
        msg = msg + " ... very lazy"
    if (v1 == "0" or v2 == "0") and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
    print(msg)


def is_one_digit(v):
    if float(v).is_integer() and -10 < float(v) < 10:
        return True
    else:
        return False


while not condition_1:
    condition_2 = False
    condition_3 = False
    condition_4 = False

    print("Enter an equation")
    eq = input().split(" ")
    x = float(0)
    y = float(0)
    result = float(0)

    if eq[0] == "M":
        eq[0] = str(memory)
    if eq[2] == "M":
        eq[2] = str(memory)

    if not eq[0].replace(".", "").isnumeric() or not eq[2].replace(".", "").isnumeric():
        print("Do you even know what numbers are? Stay focused!")
        continue
    else:
        condition_1 = True

    if not eq[1] in m_op:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        condition_1 = False
        continue

    check(eq[0], eq[2], eq[1])

    if condition_1:
        match eq[1]:
            case "+":
                result = float(eq[0]) + float(eq[2])
            case "-":
                result = float(eq[0]) - float(eq[2])
            case "*":
                result = float(eq[0]) * float(eq[2])
            case "/":
                if float(eq[2]) == 0:
                    condition_1 = False
                    print("Yeah... division by zero. Smart move...")
                    continue
                else:
                    result = float(eq[0]) / float(eq[2])

    print(result)

    while not condition_2:
        msgs = ["Are you sure? It is only one digit! (y / n)",
                "Don't be silly! It's just one number! Add to the memory? (y / n)",
                "Last chance! Do you really want to embarrass yourself? (y / n)"]
        msg_index = -1

        print("Do you want to store the result? (y / n):")
        user_input = input()

        if user_input == "y":
            if is_one_digit(result):
                msg_index = 0
                while not condition_4:
                    print(msgs[msg_index])
                    user_input_1 = input()
                    if user_input_1 == "y":
                        if msg_index < 2:
                            msg_index = msg_index + 1
                        else:
                            memory = result
                            condition_2 = True
                            condition_4 = True
                    elif user_input_1 == "n":
                        condition_2 = True
                        condition_4 = True
                        continue
                    else:
                        continue
            else:
                memory = result
                condition_2 = True
                continue
        elif user_input == "n":
            condition_2 = True
            continue
        else:
            continue

    while not condition_3:
        print("Do you want to continue calculations? (y / n):")
        user_input = input()
        if user_input == "y":
            condition_1 = False
            condition_3 = True
            continue
        elif user_input == "n":
            condition_1 = True
            condition_3 = True
            continue
        else:
            condition_3 = False

