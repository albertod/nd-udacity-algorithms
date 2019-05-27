import queue 

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group is None:
        return False

    q = queue.Queue()
    q.put(group)

    while not q.empty():
        current_group = q.get()
        if user in current_group.get_users():
            return True
        for g in current_group.get_groups():
            q.put(g)
    
    return False

print('Check sub_child_user is its groups')
print(is_user_in_group('sub_child_user', sub_child)) # True

print('Check sub_child_user is its parent groups')
print(is_user_in_group('sub_child_user', parent)) # True
print(is_user_in_group('sub_child_user', child)) # True

print('Check new user alberto is not present and then present once it is added')
print(is_user_in_group('alberto', sub_child)) # False
parent.add_user('alberto') 
print(is_user_in_group('alberto', sub_child)) # False
print(is_user_in_group('alberto', parent)) # True