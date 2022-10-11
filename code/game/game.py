from player import Player
from question import Question
from chaos_zombie import ChaosZombie
import json


class Game:

    WIN_MESSAGE = "ERFOLG! Die Zombies haben dein Gehirn gegessen. Du hast %s Fragen richtig beantwortet."
    LOOSE_MESSAGE = "NIEDERLAGE. Alle Zombies sind vorbeigezogen. Du konntest sie nicht überzeugen von deinem Wissen."

    def __init__(self):
        self.player = self.generate_player()
        self.questions = self.load_questions()
        self.zombies = self.generate_zombies()

    def generate_player(self):
        return Player(life_points=1)

    def load_questions(self):
        question_list = []
        with open('questions.json', 'r') as f:
            data = json.load(f)["questions"]
            for question in data:
                question_list.append(Question(question["text"],question["answer"]))
        return question_list

    def generate_zombies(self):
        zombies = []
        for question in self.questions:
            zombies.append(ChaosZombie(variance = 0.1, mean = 5, question = question))
        return zombies

    def game_loop(self):
        print("=== Die Zombies wollen dein Gehirn ====")
        for zombie in self.zombies:
            print(zombie.ZOMBIE_QUESTION % (zombie.name, zombie.question.text))
            print("Deine Antwort lautet:")
            player_answer = input()
            if player_answer == zombie.question.answer:
                damage = zombie.eat_brain()
                print(zombie.ZOMBIE_SUCCESS_QUESTION % damage)
                self.player.life_points -= damage
                self.player.correct_answers += 1
            else:
                print(zombie.ZOMBIE_FAIL_QUESTION)
            if self.player.life_points < 0:
                print(self.WIN_MESSAGE % self.player.correct_answers)
                return
        print(self.LOOSE_MESSAGE)

