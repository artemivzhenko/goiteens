phones = ['+38(067) 999-99-99', '+38(066) 999-99-99', '+38(067) 888-88-88', '+38(068) 777-77-77']
target_codes = {'067', '097', '068'}

count_067 = sum(1 for phone in phones if phone[4:7] == '067')
count_097 = sum(1 for phone in phones if phone[4:7] == '097')
count_068 = sum(1 for phone in phones if phone[4:7] == '068')

print("Количество абонентов с кодом 067:", count_067)
print("Количество абонентов с кодом 097:", count_097)
print("Количество абонентов с кодом 068:", count_068)
