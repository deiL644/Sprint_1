types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def remove_duplicates_and_lower_levels(tickets_dict):
    seen_tickets = set()  
    result = {}
    

    for level in range(1, 6):
        unique_tickets = []
        for ticket in tickets_dict[level]:
            if ticket not in seen_tickets:
                unique_tickets.append(ticket)
                seen_tickets.add(ticket)
        result[level] = unique_tickets
    
    return result

def create_tickets_by_type(types_dict, tickets_dict):
    cleaned_tickets = remove_duplicates_and_lower_levels(tickets_dict)
    
    tickets_by_type = {}
    for level, type_name in types_dict.items():
        tickets_by_type[type_name] = cleaned_tickets[level]
    
    return tickets_by_type

tickets_by_type = create_tickets_by_type(types, tickets)

print(tickets_by_type)