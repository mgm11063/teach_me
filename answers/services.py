from django.db import transaction
from .models import Question, Answer


def select_answer_and_award_reward(question_id, answer_id):
    with transaction.atomic():
        question = Question.objects.get(id=question_id)
        answer = Answer.objects.get(id=answer_id, question=question)

        if answer.is_accepted:
            raise ValueError("이미 선택된 답변입니다.")

        if question.reward > 0:
            answer.is_accepted = True
            answer.save()

            # 리워드 지급
            answer.user.profile.reward_points += question.reward
            answer.user.profile.save()
