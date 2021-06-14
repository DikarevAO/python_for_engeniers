if __name__ == '__main__':
    name_branch = str(input())
    
    if name_branch.capitalize() == "Development" or name_branch.capitalize() == "Staging":
        result_passing_tests = int(input())
        coverage = float(input())
        number_approve = int(input())
        is_passing_test = result_passing_tests == 1
        print(is_passing_test)
        is_coverage_or_approve = is_passing_test and (coverage > 5 or number_approve > 3)
    
        if is_coverage_or_approve:
            print(f'Внимание! Код из {name_branch} отправлен в релиз!')
        else:
            print(f'Код из {name_branch} с результатами тесты: {is_passing_test}, coverage: {coverage}, approve: '
                  f'{number_approve} в релиз не попадает. ')
    else:
        print(f'В ветке {name_branch} непроверенный код, пропускаем')