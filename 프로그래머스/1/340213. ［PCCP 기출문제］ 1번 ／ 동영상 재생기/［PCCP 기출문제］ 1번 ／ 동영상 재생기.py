def solution(video_len, pos, op_start, op_end, commands):    
    # prev: 10초 전으로 이동
    # next: 10초 후로 이동 
    # 오프닝 건너뛰기 
    
    def change_s(t):
        m, s = map(int, t.split(":"))
        return m*60 + s
    
    s_video_len = change_s(video_len)
    s_pos = change_s(pos)
    s_op_start = change_s(op_start)
    s_op_end = change_s(op_end)
    
    def op_skip(s):
        if s_op_start <= s <= s_op_end:
            s = s_op_end
        return s 
    
    for c in commands:
        s_pos = op_skip(s_pos)
        
        if c == "next":
            s_pos = min(s_video_len, s_pos+10)
            s_pos = op_skip(s_pos)
            
        elif c == "prev":
            s_pos = max(0, s_pos-10)
            s_pos = op_skip(s_pos)
    
    m = int(s_pos // 60)
    s = s_pos % 60 
    
    return (f"{m:02d}:{s:02d}")