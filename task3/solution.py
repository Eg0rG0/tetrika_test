def appearance(intervals: dict[str, list[int]]):
    events = []
    lessons = intervals["lesson"]
    pupils = intervals["pupil"]
    tutors = intervals["tutor"]

    for i in range(0, len(lessons), 2):
        events.append((lessons[i], "lesson", 1))
        events.append((lessons[i + 1], "lesson", -1))

    for i in range(0, len(pupils), 2):
        events.append((pupils[i], "pupil", 1))
        events.append((pupils[i + 1], "pupil", -1))

    for i in range(0, len(tutors), 2):
        events.append((tutors[i], "tutor", 1))
        events.append((tutors[i + 1], "tutor", -1))

    events.sort()

    active = {"lesson": 0, "pupil": 0, "tutor": 0}
    total = 0
    prev_time = None

    for time, who, delta in events:
        if prev_time is not None and all(active.values()):
            total += time - prev_time
        active[who] += delta
        prev_time = time

    return total
