def solution(record):
    user_nickname_map = {}
    entrance_map = {'Enter':'들어왔습니다.','Leave':'나갔습니다.'}
    logs = []
    for rec in record:
        parse_rec = rec.split()
        entrance,user_id = parse_rec[0],parse_rec[1]
        if entrance != 'Leave':
            user_nickname_map[user_id] = parse_rec[2]     
        
    for rec in record:
        parse_rec = rec.split()
        entrance,user_id = parse_rec[0],parse_rec[1]
        if entrance != 'Change':
            logs.append(f'{user_nickname_map[user_id]}님이 {entrance_map[entrance]}')
            
    return logs
