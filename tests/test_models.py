import unittest
from app.models import Users, Categories, Reactions, Comments, Pitches


class TestDbModels(unittest.TestCase):
    def Setup(self):
        self.user_john = Users(first_name='john', last_name='doe', email='johndoe@gmail.com', password='johnythedoe')
        self.categories = Categories(category_name='product')
        self.new_pitch = Pitches(pitch_content='Make people communicate underground', user_id=1, category_id=1)
        self.new_comment = Comments(comment='awesome idea', pitch_id=1, user_id=1)
        self.new_reaction = Reactions(reaction=1, user_id=1, pitch_id=1)

    def tearDown(self):
        Users.query.delete()
        Categories.query.delete()
        Pitches.query.delete()
        Comments.query.delete()
        Reactions.query.delete()

    def test_user_created(self):
        self.assertEqual(self.user_john.first_name, 'john')
        self.assertEqual(self.user_john.last_name, 'doe')
        self.assertEqual(self.user_john.email, 'johndoe@gmail.com')
        self.assertEqual(self.user_john.password, 'johnythedoe')


if __name__ == '__main__':
    unittest.main()
