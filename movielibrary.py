from functools import total_ordering


@total_ordering
class Movie:
    """ Represents a single Movie. """

    def __init__(self, i_title, i_date, i_runtime):
        """ Initialise a Movie Object. """
        self._title = i_title
        self._date = i_date
        self._time = i_runtime

    def __str__(self):
        """ Return a short string representation of this movie. """
        outstr = self._title
        return outstr

    def full_str(self):
        """ Return a full string representation of this movie. """
        outstr = self._title + ": "
        outstr = outstr + str(self._date) + "; "
        outstr = outstr + str(self._time)
        return outstr

    def get_title(self):
        """ Return the title of this movie. """
        return self._title

    def __eq__(self, other):
        """ Return True if this movie has exactly same title as other. """
        if (other._title == self._title):
            return True
        return False

    def __ne__(self, other):
        """ Return False if this movie has exactly same title as other. """
        return not (self._title == other._title)



    def __lt__(self, other):
        """ Return True if this movie is ordered before other.

        A movie is less than another if it's title is alphabetically before.
        """
        if other._title > self._title:
            return True
        return False


class BSTNode:
    """ An internal node for a Binary Search Tree.

    This is a general BST, but with a small number of additional methods to
    implement a movie library. The title of the Movie is used as the search
    key.
    """

    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def __str__(self):
        """ Return a string representation of the tree rooted at this node.

        The string will be created by an in-order traversal.
        """
        # method body goes here
        node = self
        if node != None:
            s = node._element._title
            if node._leftchild:
                s = node._leftchild.__str__() + s + " "
            if node._rightchild:
                s += " " + node._rightchild.__str__()
            return s
        return ' '

    def _stats(self):
        """ Return the basic stats on the tree. """
        return ('size = ' + str(self.size())
                + '; height = ' + str(self.height()))

    def search(self, title):
        """ Return the Movie object with that movie title, or None.

        This method is specific to the Movie library.
        """
        # method body goes here
        movie = self.search_node(title)
        return movie._element
        pass

    def search_node(self, searchitem):
        """ Return the node (with subtree) containing searchitem, or None. """
        # method body goes here
        if searchitem == self._element._title:
            return self
        elif searchitem < (self._element._title):
            if self._leftchild:
                return self._leftchild.search_node(searchitem)
        elif searchitem > (self._element._title):
            if self._rightchild:
                return self._rightchild.search_node(searchitem)
        else:
            return None

    def add(self, obj):
        """ Add item to the tree, maintaining BST properties.

        Returns the item added, or None if a matching object was already there.
        """
        # method body goes here
        if self._element == obj:
            return None
        elif obj < self._element:
            if not self._leftchild:
                node = BSTNode(obj)
                self._leftchild = node
                node._parent = self
                return obj
            else:
                self._leftchild.add(obj)
        else:
            if not self._rightchild:
                node = BSTNode(obj)
                self._rightchild = node
                node._parent = self
                return obj
            else:
                self._rightchild.add(obj)


    def findmaxnode(self):
        """ Return the BSTNode with the maximal element at or below here. """
        # method body goes here
        if self._rightchild:
           return self._rightchild.findmaxnode()
        else:
            return self


    def height(self):
        """ Return the height of this node.

        Note that with the recursive definition of the tree the height of the
        node is the same as the depth of the tree rooted at this node.
        """

        # method body goes here
        if self.leaf():
            return 0
        elif self.full():
            return 1 + max(self._leftchild.height(), self._rightchild.height())
        else:
            if self._leftchild:
                return 1 + (self._leftchild.height())
            else:
                return 1 + (self._rightchild.height())


    def size(self):
        """ Return the size of this subtree.

        The size is the number of nodes (or elements) in the tree.
        """
        # method body goes here
        size = 0
        if size != None:
            size += 1
        if self._leftchild != None:
            size += self._leftchild.size()
        if self._rightchild != None:
            size += self._rightchild.size()
        return size

    def leaf(self):
        """ Return True if this node has no children. """
        # method body goes here
        if self._rightchild == None and self._leftchild == None:
            return True
        else:
            return False

    def semileaf(self):
        """ Return True if this node has exactly one child. """
        # method body goes here
        if (self._leftchild == None and self._rightchild) or (self._rightchild== None and self._leftchild):
            return True
        else:
            return False

    def full(self):
        """ Return true if this node has two children. """
        # method body goes here
        if self._rightchild and self._leftchild:
            return True
        else:
            return False

    def internal(self):
        """ Return True if this node has at least one child. """
        # method body goes here
        if (self._leftchild and self._rightchild)\
                or (self._rightchild) == None and self._leftchild\
                or self._rightchild and self._leftchild == None:
            return True
        else:
            return False

    def remove(self, title):
        """ Remove and return a movie.

        This method is specific to the Movie library.
        Remove the movie with the given title from the tree rooted at this node.
        Maintains the BST properties.
        """
        # method body goes here
        movie = self.search_node(title)
        if movie is not None:
            movie.remove_node()
            return movie._element
        else:
            return None

    def remove_node(self):
        """ Remove this BSTNode from its tree, and return its element.

        Maintains the BST properties.
        """
        # if this is a full node
        # find the biggest item in the left tree
        #  - there must be a left tree, since this is a full node
        #  - the node for that item can have no right children
        # move that item up into this item
        # remove that old node, which is now a semileaf
        # return the original element
        # else if this has no children
        # find who the parent was
        # set the parent's appropriate child to None
        # wipe this node
        # return this node's element
        # else if this has no right child (but must have a left child)
        # shift leftchild up into its place, and clean up
        # return the original element
        # else this has no left child (but must have a right child)
        # shift rightchild up into its place, and clean up
        # return the original element

        # method body goes here
        old_node = self._element
        if self.full():
            old = self
            left = self._leftchild
            max_node = left.findmaxnode()
            self = max_node
            self._parent = old._parent
            if old._leftchild == self:
                pass
            else:
                self._leftchild = old._leftchild
                self._leftchild._parent = self
            if old._rightchild == self:
                pass
            else:
                self._rightchild = old._rightchild
                self._rightchild._parent = self
            if old._parent._leftchild == old:
                old._parent._leftchild = self
            else:
                old._parent._rightchild = self
            old._parent = None
            old._leftchild = None
            old._rightchild = None
            return old_node
        elif self.leaf():
            if self._element._title < self._parent._element._title:
                self._parent._leftchild = None
            elif self._element._title > self._parent._element._title:
                self._parent._rightchild = None
            self._parent = None
            return old_node
        elif self.semileaf():
            if self._leftchild:
                if not self._parent:
                    child = self._leftchild
                    self._element = child._element
                    if child._leftchild:
                        self._leftchild = child._leftchild
                    elif child._rightchild:
                        self._rightchild = child._rightchild
                    return old_node
                else:
                    old = self
                    self = self._leftchild
                    if old._parent._leftchild == old:
                        old._parent._leftchild = self
                    else:
                        old._parent._rightchild = self
                    self._parent = old._parent
                    self._leftchild._parent = self
                    old._leftchild = None
                    old._parent = None
                    return old_node
            else:
                if not self._parent:
                    child = self._rightchild
                    self._element = child._element
                    if child._leftchild:
                        self._leftchild = child._leftchild
                    else:
                        self._rightchild = child._rightchild
                    return old_node
                else:
                    old = self
                    self = self._rightchild
                    if old._parent._leftchild == old:
                        old._parent._leftchild = self
                    else:
                        old._parent._rightchild = self
                    self._parent = old._parent
                    old._rightchild = None
                    old._parent = None
                    return old_node


    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        if self._isthisapropertree() == False:
            print("ERROR: this is not a proper tree. +++++++++++++++++++++++")
        outstr = str(self._element) + ' (hgt=' + str(self.height()) + ')['
        if self._leftchild is not None:
            outstr = outstr + "left: " + str(self._leftchild._element)
        else:
            outstr = outstr + 'left: *'
        if self._rightchild is not None:
            outstr = outstr + "; right: " + str(self._rightchild._element) + ']'
        else:
            outstr = outstr + '; right: *]'
        if self._parent is not None:
            outstr = outstr + ' -- parent: ' + str(self._parent._element)
        else:
            outstr = outstr + ' -- parent: *'
        print(outstr)
        if self._leftchild is not None:
            self._leftchild._print_structure()
        if self._rightchild is not None:
            self._rightchild._print_structure()

    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree. """
        ok = True
        if self._leftchild is not None:
            if self._leftchild._parent != self:
                ok = False
            if self._leftchild._isthisapropertree() == False:
                ok = False
        if self._rightchild is not None:
            if self._rightchild._parent != self:
                ok = False
            if self._rightchild._isthisapropertree() == False:
                ok = False
        if self._parent is not None:
            if (self._parent._leftchild != self
                and self._parent._rightchild != self):
                ok = False
        return ok

    def _testadd():
        node = BSTNode(Movie("Memento", "11/10/2000", 113))
        node._print_structure()
        print('> adding Melvin and Howard')
        node.add(Movie("Melvin and Howard", "19/09/1980", 95))
        node._print_structure()
        print('> adding a second version of Melvin and Howard')
        node.add(Movie("Melvin and Howard", "21/03/2007", 112))
        node._print_structure()
        print('> adding Mellow Mud')
        node.add(Movie("Mellow Mud", "21/09/2016", 92))
        node._print_structure()
        print('> adding Melody')
        node.add(Movie("Melody", "21/03/2007", 113))
        node._print_structure()
        return node

    def _test():
        node = BSTNode(Movie("B", "b", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "A")
        node.add(Movie("A", "a", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "A")
        node.remove("A")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(Movie("C", "c", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove("C")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "F")
        node.add(Movie("F", "f", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove("B")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(Movie("C", "c", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "D")
        node.add(Movie("D", "d", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(Movie("C", "c", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "E")
        node.add(Movie("E", "e", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove("B")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "D")
        node.remove("D")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove("C")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "E")
        node.remove("E")
        print('Ordered:', node)
        node._print_structure()
        print('adding', "L")
        node.add(Movie("L", "l", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "H")
        node.add(Movie("H", "h", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "I")
        node.add(Movie("I", "i", 1))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "G")
        node.add(Movie("G", "g", 1))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "L")
        node.remove("L")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "H")
        node.remove("H")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "I")
        node.remove("I")
        print('Ordered:', node)
        node._print_structure()
        print('removing', "G")
        node.remove("G")
        print('Ordered:', node)
        node._print_structure()
        print(node)
        print(node.size())



def build_tree(filename):
    """ Return a BST tree of Movie files built from filename. """

    # open the file
    file = open(filename, 'r')

    # Create the root node  of a BST with a Movie object created from the
    # first line in the file
    inputlist = file.readline().split('\t')
    for item in inputlist:
        print(item)
    movie = Movie(inputlist[0], inputlist[1], inputlist[2])
    bst = BSTNode(movie)
    count = 1

    # now cycle through the other lines in the file, creating the Movie
    # objects and adding them to the BST
    for line in file:
        inputlist = line.split('\t')
        movie = Movie(inputlist[0], inputlist[1], inputlist[2])
        added = bst.add(movie)
        # if added != None:  # changed on 15/11/2019 - this line fails when
        #                      the BST adds a new movie, since the BST returns
        #                      a movie object, and Python then calls the
        #                      __ne__ method on the Movie class with None as
        #                      as the other argument; but None has no
        #                      _title field, and so Python crashes.
        #                      The following line works, because Python
        #                      treats 'is not' differently -- it is checking
        #                      that the two objects are different things in
        #                      in memory, regardless of their values..
        #                      You could also do     if added:
        #                      but relying on the None object to fail the
        #                      test is said to be not good coding style ...
        if added is not None:
            count += 1

    # print out some info for sanity checking
    print("Built a tree of height " + str(bst.height()))
    print("with", count, "movies")
    return bst


BSTNode._testadd()
print('++++++++++')
BSTNode._test()
print('++++++++++\n\n')
print(build_tree("smallmovies.txt"))
print('++++++++++\n\n')
print(build_tree("small_repeated_movies.txt"))
print('++++++++++\n\n')
print(build_tree("movies.txt"))


Movies = BSTNode(Movie("El Camino", "10-12-10", 122))
Movies.add(Movie("Anne", "01-01-01", 100))
Movies.add(Movie("Joker", "12-02-19", 122))
Movies.add(Movie("Midsommer", "26-05-10", 138))
Movies.add(Movie("Cinderella", "02-02-02", 129))
Movies.add(Movie("Donny Darko", "03-03-03", 129))
MeanGirls = Movie("Mean Girls", "04-04-04", 209)