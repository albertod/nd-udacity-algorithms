# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler, not_found_handler):
        self.root = RouteTrieNode(root_handler)
        self.not_found_handler = (
            not_found_handler
        )  # to return in case we don't find the path

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        cursor = self.root
        for path in path_list:
            if path not in cursor.childs:
                cursor.insert(path)
            cursor = cursor.childs[path]
        # new leaf -> add handler
        cursor.handler = handler

    def find(self, path_list):
        cursor = self.root
        for path in path_list:
            if path not in cursor.childs:
                return None
            cursor = cursor.childs[path]
        return cursor.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.childs = {}

    def insert(self, path, handler=None):
        self.childs[path] = RouteTrieNode()

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        self.route_trie = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, path_string, handler):
        path = self.split_path(path_string)
        self.route_trie.insert(path, handler)

    def lookup(self, path_string):
        path = self.split_path(path_string)
        result = self.route_trie.find(path)
        if result:
            return result
        else:
            return self.route_trie.not_found_handler

    def split_path(self, path_string):
        """
        Return the path between root_path '/' and then '/' (both are not inclusive)
        1) / -> []
        2) /about -> ['about']
        3) /about/me/ ['about', 'me']
        4) about -> []
        """
        if len(path_string) == 0:
            return []  # handle empty path
        path_list = path_string.split("/")
        if path_list[0] == "":
            path_list = path_list[1:]  # Remove prefix '/'
        if path_list[-1] == "":
            path_list = path_list[0:-1]  # Remove trailing '/'
        return path_list


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router(
    "root handler", "not found handler"
)  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# # some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/me"))  # should print 'not found handler' or None if you did not implement one