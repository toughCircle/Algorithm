def solution(n):
    answer = []
    
    def move_disks(num_disks, start, target, auxiliary):
        if num_disks == 1:
            answer.append([start, target])
            return
        # n-1개의 원판을 보조 기둥으로 이동
        move_disks(num_disks - 1, start, auxiliary, target)
        # 가장 큰 원판을 목표 기둥으로 이동
        answer.append([start, target])
        # 보조 기둥의 원판들을 목표 기둥으로 이동
        move_disks(num_disks - 1, auxiliary, target, start)

    # 1 = 시작, 2 = 보조, 3 = 도착
    move_disks(n, 1, 3, 2)

    return answer