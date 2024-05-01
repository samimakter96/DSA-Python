class Akhilesh:
    Back = "Oracle DB & Java"

    def back_end(self):
        print("Backend Task implemented using: ", self.Back)


class Ankit:
    Front = "HTML CSS Javascript"

    def front_end(self):
        print("Frontend Task implemented using: ", self.Front)


class TeamLead(Akhilesh, Ankit):
    def show(self):
        print("Dynamic Website Created")


T = TeamLead()
T.back_end()
T.front_end()
T.show()