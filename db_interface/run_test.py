import os

if __name__ == "__main__":
    test = os.listdir('./tests')

    tests_dict = {}
    list_tests = ''
    iel = 1
    for el in test:
        if el[-3:]=='.py':
            l = f"{iel}:  {el}\n"
            list_tests += l
            tests_dict[str(iel)] = el
            iel += 1

    print('List of tests:')
    print('*'*80)
    print(list_tests)

    var = input("Enter the ID of the test to run: ")

    print(f"Running the test #{var}: {tests_dict[var]}")


    os.system(f"python3 {os.path.join('./tests',tests_dict[var])}")

