try:
    amount=int(input('Enter the amount: '))
    if amount<0:
        raise ValueError('Enter the positive number..')

except Exception as e:
    print(f'Error occured: {e}')

else:
    print('No errors..')
    print('u can withdraw..')
finally:
    print('---remove u r card---')