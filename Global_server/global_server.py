import socket
import re

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((socket.gethostname(), 8086))
s.listen(1)
print("Waiting for conection .....")

while True:
    client_socket, client_adr = s.accept()
    print(f"connection from {client_adr} has been establisted")

    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADER_SIZE}}" + msg

    client_socket.send(bytes(msg, "utf-8"))

    filename = input(str("Please enter a lab name file: "))
    file = open(filename, 'wb')
    filedata = client_socket.recv(1024)
    file.write(filedata)
    temp = str(filedata).lower()

    print("File with lab data received succesfully!")

    cont = input(str("Update record? (y/n) "))
    if cont == 'n':
        reset_ques = input(str("Do you want to reset lab record? (y/n) "))
        if reset_ques == 'n':
            file.close()
            break
        else:
            reset_file = open(f'reset.txt', 'r+')
            reset_filedata = str(reset_file.read()).lower()

            lab_id = int(input("enter lab ID: "))

            if lab_id == 1:
                file_init = open(f'init1.txt', 'w+')
                file_init.write(reset_filedata)
                file_init.close()
            elif lab_id == 2:
                file_init = open(f'init2.txt', 'w+')
                file_init.write(reset_filedata)
                file_init.close()
            elif lab_id == 3:
                file_init = open(f'init3.txt', 'w+')
                file_init.write(reset_filedata.encode())
                file_init.close()
            reset_file.close()
            file.close()
        break
    else:

        # getting ingeters value from saved lab file
        checker = list(re.findall(r'\d+', temp))
        infected_count = int(checker[0])
        death_count = int(checker[1])
        recovered_count = int(checker[2])
        print(infected_count, death_count, recovered_count)

        lab_id = int(input("enter lab ID: "))

        if (lab_id == 1):
            file_init = open(f'init1.txt', 'r+')
            filedata_init = str(file_init.read()).lower()
            lists = list(re.findall(r'\d+', filedata_init))
            infected_count_init = int(lists[0])
            death_count_init = int(lists[1])
            recovered_count_init = int(lists[2])
            file_init.close()

            if ((infected_count_init <= infected_count) and (death_count_init <= death_count) and (recovered_count_init <= recovered_count)):
                file_init = open(f'init1.txt', 'wb+')
                file_init.write(filedata)
                file_init.close()

        elif (lab_id == 2):
            file_init = open(f'init2.txt', 'r+')
            filedata_init = str(file_init.read()).lower()
            lists = list(re.findall(r'\d+', filedata_init))
            infected_count_init = int(lists[0])
            death_count_init = int(lists[1])
            recovered_count_init = int(lists[2])
            file_init.close()
            print(infected_count_init, death_count_init, recovered_count_init)

            if ((infected_count <= infected_count) and (death_count_init <= death_count) and (recovered_count_init <= recovered_count)):
                file_init = open(f'init2.txt', 'wb+')
                file_init.write(filedata)
                file_init.close()
        elif (lab_id == 3):
            file_init = open(f'init3.txt', 'r+')
            filedata_init = str(file_init.read()).lower()
            lists = list(re.findall(r'\d+', filedata_init))
            infected_count_init = int(lists[0])
            death_count_init = int(lists[1])
            recovered_count_init = int(lists[2])
            file_init.close()

            if ((infected_count <= infected_count) and (death_count_init <= death_count) and (recovered_count_init <= recovered_count)):
                file_init = open(f'init3.txt', 'wb+')
                file_init.write(filedata)
                file_init.close()
        file.close()
        break

s.close()
