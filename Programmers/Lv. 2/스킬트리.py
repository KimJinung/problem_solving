def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        if is_valid_skill_tree(skill, tree):
            answer += 1

    return answer


def is_valid_skill_tree(order: str, skill_tree: str) -> bool:
    skill_dict = {}

    skill_stack = []

    for idx, skill in enumerate(order):

        # Set prerequisite skills for current skill
        skill_dict[skill] = list(order[:idx])

    for skill in skill_tree:
        prerequisite = skill_dict.get(skill)

        if prerequisite is not None:

            # Check current prerequisite skill stack
            if skill_stack != prerequisite:
                return False

            skill_stack.append(skill)

    return True
