def solution(emergency):
    return [{v:k+1 for k, v in enumerate(sorted(emergency, reverse=True))}[i] for i in emergency]