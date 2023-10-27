def find_common_participants(participants_first_group, participants_second_group, sep=','):
    common_participants = list(set(participants_first_group.split(sep)) & set(participants_second_group.split(sep)))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
