import pytest

class Testlab:

    def test_one(self):
        right_answ = ['+1 (958) 5586234', '+1 (216) 8748522', '+1 (646) 5474621']
        f = open("Answer.txt", "r")
        liste = f.read().splitlines()
        for i in range(len(liste)):
            if (liste[i]!=right_answ[i]):
                assert 0
        assert 1
