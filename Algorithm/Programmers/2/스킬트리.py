def solution(skill, skill_trees):
    skills = skill

    answer = 0

    prerequisite_dict = {}

    for idx, skill in enumerate(skills):
        prerequisite_dict[skill] = list(skills[:idx])

    for tree in skill_trees:
        if is_valid_skill_tree(prerequisite_dict, tree):
            answer += 1

    return answer


def is_valid_skill_tree(prerequisites: dict, skill_tree: str) -> bool:
    skill_stack = []

    for skill in skill_tree:
        prerequisite = prerequisites.get(skill)

        if prerequisite is not None:  # Check current prerequisite skill stack
            if skill_stack != prerequisite:
                return False

            skill_stack.append(skill)

    return True
