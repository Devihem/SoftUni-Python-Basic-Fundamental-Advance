free_columns = ['1','2','3','4','5','6','7','8','9','10','11']
free_columns = [' '+x if len(x) == 1 else x for x in free_columns ]
print('┌─' + '───┬─' * (len(free_columns) - 1) + '───┐')

print('│ ' + ' │ '.join(free_columns), end=' │')

# Bottom frame
print('\n└─' + '───┴─' * (len(free_columns) - 1) + '───┘', end='')
