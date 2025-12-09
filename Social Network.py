class User:
    def __init__(self, username, email):
        self.__username = username
        self.__email = email
        self.__subscriptions = set()  # кімге жазылған
        self.posts = []  # қолданушының посттары

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def subscribe(self, other_user):
        if other_user != self:
            self.__subscriptions.add(other_user)
            print(f"{self.__username} {other_user.get_username()} жазылды!")

    def unsubscribe(self, other_user):
        self.__subscriptions.discard(other_user)
        print(f"{self.__username} {other_user.get_username()} жазылымды тоқтатты!")

    def create_post(self, content):
        post = Post(author=self, content=content)
        self.posts.append(post)
        return post

    def show_subscriptions(self):
        print(f"{self.__username} жазылғандар:")
        for u in self.__subscriptions:
            print("-", u.get_username())
class Post:
    def __init__(self, author: User, content: str):
        self.author = author
        self.content = content
        self.comments = []
        self.likes = set()  # кім лайктады

    def add_comment(self, comment):
        self.comments.append(comment)

    def like(self, user: User):
        self.likes.add(user)
        print(f"{user.get_username()} лайк жасады!")

    def unlike(self, user: User):
        self.likes.discard(user)
        print(f"{user.get_username()} лайкты алып тастады!")

    def show_post(self):
        print(f"Автор: {self.author.get_username()}")
        print(f"Мәтін: {self.content}")
        print(f"Лайктар саны: {len(self.likes)}")
        if self.comments:
            print("Комментарии:")
            for c in self.comments:
                print(f" - {c.author.get_username()}: {c.text}")
class Comment:
    def __init__(self, author: User, text: str):
        self.author = author
        self.text = text
# Қолданушылар
user1 = User("Mustafa", "elaman@mail.com")
user2 = User("Nur", "aigerim@mail.com")
user3 = User("Umit", "serik@mail.com")

# Жазылымдар
user1.subscribe(user2)
user1.subscribe(user3)
user2.subscribe(user1)

user1.show_subscriptions()

# Пост жасау
post1 = user1.create_post("Бүгінгі күн керемет!")
post2 = user2.create_post("Мен жаңа кітап оқып жатырмын.")

# Лайк және комментарий
post1.like(user2)
post1.like(user3)

comment1 = Comment(author=user2, text="Тамаша!")
comment2 = Comment(author=user3, text="Керемет жазылған!")

post1.add_comment(comment1)
post1.add_comment(comment2)

# Постты көрсету
post1.show_post()
post2.show_post()
