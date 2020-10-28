import tkinter as tk

LARGE_FONT = ("Verdana", 19)
SMALL_FONT = ("Times", 14)
BIG_FONT = ("Times", 25)


class python(tk.Tk):

    def __init__(self, *args, **kwargs):  # __init__ function for class python

        tk.Tk.__init__(self, *args, **kwargs)  # __init__ function for class TK
        container = tk.Frame(self)  # creating a container

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # setting frames to an empty array

        for F in (
        subjectPage, maths, science, whole_numbers, pre_suce, prop, clo_prop, comu_prop, asso_prop, dis_prop, iden_prop,
        play_num, fact_num, pri_num, com_div, fun_mag, fibr, elec, english, tense, past, present, future):
            frame = F(container, self)

            self.frames[F] = frame  # iterating a tuple consisting of pagelayouts

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(subjectPage)

    def show_frame(self, cont):
        frame = self.frames[cont]  # displaying current frame passed as parameter
        frame.tkraise()


class subjectPage(tk.Frame):  # first window frame subjectpage

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to 5th CBSE", font=BIG_FONT)
        label.pack(pady=10, padx=10)  # labeling the text

        label = tk.Label(self, text="Select your Subject:", font=LARGE_FONT)
        label.pack(pady=15, padx=5)
        # assigning buttons in subjet page to switch to the chapter page
        button = tk.Button(self, text="MATHEMATICS",
                           command=lambda: controller.show_frame(maths))
        button.pack()

        button2 = tk.Button(self, text="SCIENCE",
                            command=lambda: controller.show_frame(science))
        button2.pack()
        button3 = tk.Button(self, text="ENGLISH",
                            command=lambda: controller.show_frame(english))
        button3.pack()


class maths(tk.Frame):  # for chapters in maths window

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MATHEMATICS", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="Select chapter", font=LARGE_FONT)
        label.pack(pady=15, padx=5)

        button1 = tk.Button(self, text="whole numbers",  # assigning buttons for topics to move into another windows
                            command=lambda: controller.show_frame(whole_numbers))
        button1.pack()

        button2 = tk.Button(self, text="playing with numbers",
                            command=lambda: controller.show_frame(play_num))
        button2.pack()

        button3 = tk.Button(self, text="Common Divisors",
                            command=lambda: controller.show_frame(com_div))
        button3.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()


class science(tk.Frame):

    def __init__(self, parent, controller):  # __init__ function for function science
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="SCIENCE", font=LARGE_FONT)
        label.pack(pady=10, padx=10)  # labeling the text

        label = tk.Label(self, text="select chapter:", font=LARGE_FONT)
        label.pack(pady=15, padx=5)

        button1 = tk.Button(self, text="fun with magnets",  # assigning buttons to move into another windows
                            command=lambda: controller.show_frame(fun_mag))
        button1.pack()

        button2 = tk.Button(self, text="fibre to fabric",
                            command=lambda: controller.show_frame(fibr))
        button2.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(elec))
        button3.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()


class whole_numbers(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="WHOLE NUMBERS", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="Select topic", font=LARGE_FONT)
        label.pack(pady=15, padx=5)

        button1 = tk.Button(self, text="predessecor and successor",
                            command=lambda: controller.show_frame(pre_suce))
        button1.pack()

        button2 = tk.Button(self, text="properties of whole numbers",
                            command=lambda: controller.show_frame(prop))
        button2.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()


class pre_suce(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PRERDECESSOR:-", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="We can obtain predecessor by subracting 1 from any given number\nfor example:-",
                         font=SMALL_FONT)
        label.pack(pady=14, padx=5)

        label = tk.Label(self,
                         text="if we got the number 25949 we have to do 25949-1 to this\nso we got 25948\nso,this is the predecessor of the given number",
                         font=SMALL_FONT)
        label.pack(pady=17, padx=5)

        label = tk.Label(self, text="SUCCESSOR:-", font=LARGE_FONT)
        label.pack(pady=21, padx=10)

        label = tk.Label(self, text="We can obtain Successor by Adding 1 from any given number\nfor example:-",
                         font=SMALL_FONT)
        label.pack(pady=23, padx=5)

        label = tk.Label(self,
                         text="if we got the number 25949 we have to do 25949+1 to this\nso we got 25950\nso,this is the Successor of the given number",
                         font=SMALL_FONT)
        label.pack(pady=25, padx=5)

        button1 = tk.Button(self, text="Back to Topics",
                            command=lambda: controller.show_frame(whole_numbers))
        button1.pack()

        button2 = tk.Button(self, text="Back to Subject Page",
                            command=lambda: controller.show_frame(subjectPage))
        button2.pack()


class prop(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PROPERTIES OF WHOLE NUMBERS:-", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="The propeties of whole numbers includes :", font=SMALL_FONT)
        label.pack(pady=12, padx=5)

        button1 = tk.Button(self, text="Closure Property",
                            command=lambda: controller.show_frame(clo_prop))
        button1.pack()

        button2 = tk.Button(self, text="Commutative property",
                            command=lambda: controller.show_frame(comu_prop))
        button2.pack()

        button3 = tk.Button(self, text="Associative Property",
                            command=lambda: controller.show_frame(asso_prop))
        button3.pack()

        button4 = tk.Button(self, text="Distributive Property",
                            command=lambda: controller.show_frame(dis_prop))
        button4.pack()

        button5 = tk.Button(self, text="Identity Property",
                            command=lambda: controller.show_frame(iden_prop))
        button5.pack()

        button1 = tk.Button(self, text="Back to Topics",
                            command=lambda: controller.show_frame(whole_numbers))
        button1.pack()

        button2 = tk.Button(self, text="Back to Subject Page",
                            command=lambda: controller.show_frame(subjectPage))
        button2.pack()


class clo_prop(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CLOSURE PROPPERTY:-", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="The closure property is a simple one. when we add or multiply any \ntwo whole numbers the answer have to be whole number.",
                         font=SMALL_FONT)
        label.pack(pady=12, padx=5)

        label = tk.Label(self, text="for example:-", font=LARGE_FONT)
        label.pack(pady=13, padx=5)

        label = tk.Label(self, text="3+5=8,45+0=45,6+9=15", font=LARGE_FONT)
        label.pack(pady=14, padx=5)

        button1 = tk.Button(self, text="Back to Topics",
                            command=lambda: controller.show_frame(whole_numbers))
        button1.pack()

        button2 = tk.Button(self, text="Back to Subject Page",
                            command=lambda: controller.show_frame(subjectPage))
        button2.pack()

        button2 = tk.Button(self, text="Back to Properties",
                            command=lambda: controller.show_frame(prop))
        button2.pack()


class comu_prop(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="COMMUTATIVE PROPPERTY:-", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="You can add whole nos. in any order.\n We can say that addition is commutative for whole numbers\n. This property is known as commutativity for addition.",
                         font=SMALL_FONT)
        label.pack(pady=12, padx=5)

        label = tk.Label(self,
                         text="for example :-\n11+4=4+11 is 15=15\n8*6=6*8 is 48=48\nThese  are commutative properties",
                         font=SMALL_FONT)
        label.pack(pady=13, padx=5)

        button1 = tk.Button(self, text="Back to Topics",
                            command=lambda: controller.show_frame(whole_numbers))
        button1.pack()

        button2 = tk.Button(self, text="Back to Subject Page",
                            command=lambda: controller.show_frame(subjectPage))
        button2.pack()

        button2 = tk.Button(self, text="Back to Properties",
                            command=lambda: controller.show_frame(prop))
        button2.pack()


class asso_prop(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ASSOCIATIVE PROPPERTY:-", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="In the 1st , you can add 5 and 7 first and then add 3 to the sum\nand in 2nd , you can add 7 and 3 first\nand then add 5 to the sum.\nThe result in both the cases are same.",
                         font=SMALL_FONT)
        label.pack(pady=13, padx=5)

        label = tk.Label(self,
                         text="Observe the following examples :\n1) (5 + 7 ) + 3 = 12 + 3 = 15\n2) 5 + (7 + 3) = 5 + 10 = 15",
                         font=SMALL_FONT)
        label.pack(pady=14, padx=5)

        button1 = tk.Button(self, text="Back to Topics",
                            command=lambda: controller.show_frame(whole_numbers))
        button1.pack()

        button2 = tk.Button(self, text="Back to Subject Page",
                            command=lambda: controller.show_frame(subjectPage))
        button2.pack()

        button2 = tk.Button(self, text="Back to Properties",
                            command=lambda: controller.show_frame(prop))
        button2.pack()


class dis_prop(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="DISTRIBUTIVE PROPPERTY:-", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="35 x (98+2)=35 x 100=3500\n65 x (48 + 2) = 65 x 50 = 3250\n297 x 17 + 297 x 3 = 297 x (17 + 3) = 297 x 20 = 5940\nAll the above are the examples of distributive property of\n multiplication over addition.",
                         font=SMALL_FONT)
        label.pack(pady=13, padx=5)

        button1 = tk.Button(self, text="Back to Topics",
                            command=lambda: controller.show_frame(whole_numbers))
        button1.pack()

        button2 = tk.Button(self, text="Back to Subject Page",
                            command=lambda: controller.show_frame(subjectPage))
        button2.pack()

        button2 = tk.Button(self, text="Back to Properties",
                            command=lambda: controller.show_frame(prop))
        button2.pack()


class iden_prop(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="IDENTITY PROPPERTY:-", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="Zero is called an Identity for addition of whole numbers\nor additive identity for whole numbers.\nfor example:-\n8+0=8,0+5=5\nThese are Addititive property",
                         font=SMALL_FONT)
        label.pack(pady=13, padx=5)

        label = tk.Label(self,
                         text="1 is called identity for multiplication of whole numbers\n or multiplicative identity for whole numbers.\n for example:-\n 1*56=56,45*1=45\n These are Multiplicative Identity ",
                         font=SMALL_FONT)
        label.pack(pady=14, padx=5)

        button1 = tk.Button(self, text="Back to Topics",
                            command=lambda: controller.show_frame(whole_numbers))
        button1.pack()

        button2 = tk.Button(self, text="Back to Subject Page",
                            command=lambda: controller.show_frame(subjectPage))
        button2.pack()

        button2 = tk.Button(self, text="Back to Properties",
                            command=lambda: controller.show_frame(prop))
        button2.pack()


class play_num(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PLAYING WITH NUMBERS TOPICS", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2 = tk.Button(self, text="Factors of a number",
                            command=lambda: controller.show_frame(fact_num))
        button2.pack()

        button2 = tk.Button(self, text="Prime and composite numbers",
                            command=lambda: controller.show_frame(pri_num))
        button2.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()

        button3 = tk.Button(self, text="Back to chapters",
                            command=lambda: controller.show_frame(maths))
        button3.pack()


class fact_num(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Factors of a Number", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="Factors of a number are defined as numbers or algebraic expressions that divide\n a given number or expression evenly.\n We can also say, factors are the numbers\n which are multiplied to get the other number.",
                         font=SMALL_FONT)
        label.pack(pady=12, padx=5)

        label = tk.Label(self, text="For example, 1, 3 and 9 are the factors of 9, because 1 × 9 = 9 and 3 × 3 = 9.",
                         font=SMALL_FONT)
        label.pack(pady=14, padx=5)

        label = tk.Label(self,
                         text="Step 1: Choose a number (say, 16)\n Step 2: Write the common factors of 16 which will include (16 × 1), (-16 × -1), (8 × 2), (-8 × -2), (4 × 4), and (-4 × -4).\n Step 3: Further factor the factors until a prime number is reached.",
                         font=SMALL_FONT)
        label.pack(pady=16, padx=5)

        label = tk.Label(self,
                         text="Step 4: Write down all the factors again. The (8 × 2) will now become (4 × 2 × 2).\n Step 5: Write all the unique number that is obtained.",
                         font=SMALL_FONT)
        label.pack(pady=18, padx=5)

        button3 = tk.Button(self, text="Back to chapters",
                            command=lambda: controller.show_frame(maths))
        button3.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()

        label = tk.Label(self,
                         text="you can also watch video by clicking the given link:- \n https://youtu.be/k3HRISHhX-s",
                         font=SMALL_FONT)
        label.pack(pady=10, padx=10)


class pri_num(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PRIME AND COMPOSITE NUMBERS", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="Prime numbers are the positive integers having only \n two factors, 1 and the integer itself.\nFor Example:-",
                         font=LARGE_FONT)
        label.pack(pady=12, padx=5)

        label = tk.Label(self,
                         text="For example, factors of 6 are 1,2,3 and 6, which are four factors in total.\n But factors of 7 are only 1 and 7, totally two. Hence, 7 is a prime number\n but 6 is not, instead it is a composite number. But always remember that \n1 is neither prime nor composite.",
                         font=SMALL_FONT)
        label.pack(pady=14, padx=5)

        label = tk.Label(self, text="COMPOSITE NUMBERS:-", font=SMALL_FONT)
        label.pack(pady=16, padx=5)

        label = tk.Label(self,
                         text="A composite number has more than two factors.\n It can be divided by all its factors.\n For example, 6 is divisible by 2,3 and 6.\n Examples: 4, 8, 10, 15, 85, 114, 184, etc.",
                         font=SMALL_FONT)
        label.pack(pady=18, padx=5)

        button3 = tk.Button(self, text="Back to chapters",
                            command=lambda: controller.show_frame(maths))
        button3.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()


class com_div(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="COMMON DIVISORS", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="The greatest common divisor (GCD) or highest common factor (HCF) of two numbers is the\n largest number that divides both the two numbers exactly.",
                         font=SMALL_FONT)
        label.pack(pady=12, padx=5)

        label = tk.Label(self,
                         text="Prime Factorization:-\n N the prime factorisation method, each given number is written as the product of prime\n numbers and then find the product of the smallest power\n of each common prime factor.\nThis method is applicable only for positive numbers, i,e. Natural numbers.",
                         font=SMALL_FONT)
        label.pack(pady=14, padx=5)

        label = tk.Label(self,
                         text="Long Division Method:-\n In this method, the largest number among the given set of numbers should be divided \n by the second largest number, and again the second largest\n number should be divided by the remainder \n of the previous operation, this process will continue till the remainder is zero",
                         font=SMALL_FONT)
        label.pack(pady=16, padx=5)

        button3 = tk.Button(self, text="Back to chapters",
                            command=lambda: controller.show_frame(maths))
        button3.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()


class fun_mag(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="FUN WITH MAGNETS \n ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="Magnet: An object which attracts magnetic materials; like iron, cobalt and nickel; is called magnet.",
                         font=SMALL_FONT)
        label.pack(pady=12, padx=5)

        label = tk.Label(self,
                         text="Magnetic Materials: Materials which are attracted towards a magnet are called magnetic materials,\n e.g. iron, nickel and cobalt.\nNon-magnetic Materials: Materials which are not attracted towards a magnet are called non-magnetic materials, e.g. aluminium, zinc, wood, rubber, etc.",
                         font=SMALL_FONT)
        label.pack(pady=14, padx=5)

        label = tk.Label(self,
                         text="Poles of a Magnet: A magnet has two poles, viz. north pole and south pole. \nThe magnetic power is concentrated on the poles of a magnet. \nWhen a bar magnet is suspended to move freely, it always points in the north-south direction.\n The north pole of the magnet points towards the north and the south pole of the magnet points\n towards the south. ",
                         font=SMALL_FONT)
        label.pack(pady=16, padx=5)

        label = tk.Label(self,
                         text="INTERACTION OF MAGNETS\nLike poles repel each other. \nThis means when north pole of a magnet is brought near the north pole of another magnet,\n both repel each other.\n The same holds true for the south poles of two magnets. ",
                         font=SMALL_FONT)
        label.pack(pady=18, padx=5)

        label = tk.Label(self,
                         text="Unlike poles attract each other.\n This means when north pole of a magnet is\n brought near the south pole of another magnet,\n both attract each other. ",
                         font=SMALL_FONT)
        label.pack(pady=20, padx=5)

        button3 = tk.Button(self, text="Back to Chapters",
                            command=lambda: controller.show_frame(science))
        button3.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()


class fibr(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="FIBRE TO FABRIC ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="Fibres: \n The thin threads or filaments which form a yarn are called Fibres.VARIETY OF FIBRES:- \nYARN: Yarn is defined as a long, twisted and continuous strand composed of \n interlocked fibres or filaments which are used in knitting and weaving\n to form cloth.",
                         font=SMALL_FONT)
        label.pack(pady=12, padx=10)

        label = tk.Label(self,
                         text="COTTON:-\nCotton plants are grown in fields usually at places having a warm climate and black soil.\nCotton plants bear fruits the size of a lemon called Cotton Balls which burst open\n upon maturing and the seeds wrapped up in cotton fibre become \n visible. Cotton is generally picked by hand from these balls. ",
                         font=SMALL_FONT)
        label.pack(pady=14, padx=5)

        label = tk.Label(self,
                         text="JUTE:-\n Jute fibre is obtained from the stem of the plant.\n Unlike cotton, jute is cultivated in the rainy season.\n The plant is harvested during its flowering stage.\nThe stems of these harvested plants are then soaked in water for four to five days",
                         font=SMALL_FONT)
        label.pack(pady=16, padx=5)

        button3 = tk.Button(self, text="Back to Chapters",
                            command=lambda: controller.show_frame(science))
        button3.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()


class elec(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ELECTRICITY", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="Electricity is the powerful form of energy. All the devices which run by electricity have an electric current flow through them. \nSome examples are the electric bulb, heater, refrigerator, iron, fan, oven etc.",
                         font=SMALL_FONT)
        label.pack(pady=13, padx=5)

        label = tk.Label(self,
                         text="ELECTRICITY CELL:-\n  There are two terminals- metal cap for positive and metal disc for negative. \nThe electric current is produced through the chemical present in it.\n Electric cells are used in may devices like a torch, alarm clock, wristwatch, radios, camera and many other devices",
                         font=SMALL_FONT)
        label.pack(pady=15, padx=5)

        label = tk.Label(self,
                         text="ELECTRIC CIRCUIT:-\nElectricity flows through the positive terminal to negative terminal through a path. \n A connection is required outside the electric cell that can support the flow of \n current from positive to negative terminal of the cell.\n The path through which connection is passed is known as an electric circuit.",
                         font=SMALL_FONT)
        label.pack(pady=17, padx=5)

        label = tk.Label(self,
                         text="CONDUCTORS:-\n Conductors are the materials which allow current to flow through them.\nEXAMPLE:-\n  All metal wires, non-metal like graphite, gas carbon, the solution of acids in water, solution alkali in water, the solution of salts in water etc.",
                         font=SMALL_FONT)
        label.pack(pady=19, padx=5)

        label = tk.Label(self,
                         text="INSULATOR:-\n Insulators are the materials which do not allow current to flow through them.\n Example-\n rubber, plastic paper, petrol, diesel, alcohol etc.",
                         font=SMALL_FONT)
        label.pack(pady=20, padx=5)

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()

        button3 = tk.Button(self, text="Back to chapters",
                            command=lambda: controller.show_frame(science))
        button3.pack()


class english(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="English", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self, text="Select Chapter of your Choice:-", font=LARGE_FONT)
        label.pack(pady=12, padx=5)

        button3 = tk.Button(self, text="Nouns",
                            command=lambda: controller.show_frame(noun))
        button3.pack()

        button3 = tk.Button(self, text="Tenses",
                            command=lambda: controller.show_frame(tense))
        button3.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()


class noun(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NOUNS", font=BIG_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self,
                         text="Noun is the name of a person, place, animal or things. All naming \nwords such as boy, girl, Delhi, cow,",
                         font=SMALL_FONT)
        label.pack(pady=12, padx=5)
        label = tk.Label(self, text="Types of Nouns:", font=LARGE_FONT)
        label.pack(pady=14, padx=5)
        label = tk.Label(self,
                         text="PROPER NOUN:-\nA Proper Noun is the special name of a particular person or place\n example:-\ni live in mumbai\nCOMMON NOUN:-\n A Common Noun is a name given in common to every person or \nthing of the same class or kind.\nexample:\nit is a beautiful park.",
                         font=SMALL_FONT)
        label.pack(pady=16, padx=5)

        label = tk.Label(self,
                         text="COLLECTIVE NOUN:-\nWhen a noun stands for a collection of persons or things,considered as one complete whole, \nit is called Collective Noun.\nExample:-\nI saw a herd of cattle.",
                         font=LARGE_FONT)
        label.pack(pady=18, padx=5)
        label = tk.Label(self,
                         text="MATERIAL NOUN:-\nA noun which stands for the matter or\n substance of which things are made is called Material Noun.\nExample:-\nThe chain is made of gold.",
                         font=SMALL_FONT)
        label.pack(pady=20, padx=5)
        label = tk.Label(self,
                         text="ABSTRACT NOUN:-\nAn Abstract Noun is the name given to a quality, a state or a concept.\n These are something which we can neither see nor touch but which we\n can only feel or think of them.\n Example:\nI always speak the truth.",
                         font=SMALL_FONT)
        label.pack(pady=22, padx=5)

        button3 = tk.Button(self, text="Back to chapters",
                            command=lambda: controller.show_frame(english))
        button3.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()


class tense(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="TYPES OF TENSES:", font=BIG_FONT)
        label.pack(pady=10, padx=10)

        button3 = tk.Button(self, text="Past Tense",
                            command=lambda: controller.show_frame(past))
        button3.pack()

        button3 = tk.Button(self, text="Present Tense",
                            command=lambda: controller.show_frame(present))
        button3.pack()

        button3 = tk.Button(self, text="Future Tense",
                            command=lambda: controller.show_frame(future))
        button3.pack()

        button3 = tk.Button(self, text="Back to chapters",
                            command=lambda: controller.show_frame(english))
        button3.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()


class past(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PAST TENSE", font=BIG_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="SIMPLE PAST:-\n Simple past tense is used to denote a single action in the past.\nExample:-\nThe ship sailed yesterday.\n Structure :- Sub + V2",
                         font=SMALL_FONT)
        label.pack(pady=12, padx=5)
        label = tk.Label(self,
                         text="PAST CONTINOUS TENSE:-\nThe past continuous tense represents an action as going on\n at some point of time in the past\nEXAMPLE:-\nI was reading, when he called on me.\n Structure:- Subject + was / were + V4",
                         font=SMALL_FONT)
        label.pack(pady=14, padx=5)
        label = tk.Label(self,
                         text="PAST PERFECT TENSE:-\n The Past Perfect Tense denotes an action completed before \n a certain moment in the past\nExample:-\nHe had already read this book.\n Structure:-  Subject + had + V3 + object",
                         font=SMALL_FONT)
        label.pack(pady=16, padx=5)
        label = tk.Label(self,
                         text="PAST PERFECT CONTINOUS TENSE:-\nExample:-\nHe had not been meeting me for a month.\nStructure:- Subject + had been + V4 (V1 + ing)",
                         font=SMALL_FONT)
        label.pack(pady=18, padx=5)

        button3 = tk.Button(self, text="Back to chapters",
                            command=lambda: controller.show_frame(english))
        button3.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()
        button3 = tk.Button(self, text="Back to tenses",
                            command=lambda: controller.show_frame(tense))
        button3.pack()


class present(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PRESENT TENSE", font=BIG_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="SIMPLE PRESENT TENSE:-\n To express what is actually taking place at the present moment\n Structure:- Subject + V1/Vs (s or es)",
                         font=SMALL_FONT)
        label.pack(pady=12, padx=5)
        label = tk.Label(self,
                         text="PRESENT CONTINOUS TENSE:- \nThe Present Continuous Tense represents an action as going on at the time of speaking\nEXAMPLE:-\n I am opening the door.\n Structure:- Subject + is / am / are + V4 (V1 + ing)",
                         font=SMALL_FONT)
        label.pack(pady=14, padx=5)
        label = tk.Label(self,
                         text="PRESENT PERFECT TENSE :-\n The Present Perfect Tense denotes an action that has just been completed\n EXAMPLE:-\n I have written my essay.\n Structure:-\nSubject + has / have + V3",
                         font=SMALL_FONT)
        label.pack(pady=16, padx=5)
        label = tk.Label(self,
                         text="PRESENT PERFECT CONTINOUS TENSE:- Sometimes an action, beginning in the past, is still continuing at the present moment. \n This frequently happens with verbs such as stay, wait, sit, stand, lie, study, learn, live, rest etc\n EXAMPLE:-\nHe has been here for one day.\nStructure:-Subject + has / have been + V4(V1 + ing\n) ",
                         font=SMALL_FONT)
        label.pack(pady=18, padx=5)

        button3 = tk.Button(self, text="Back to chapters",
                            command=lambda: controller.show_frame(english))
        button3.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()
        button3 = tk.Button(self, text="Back to tenses",
                            command=lambda: controller.show_frame(tense))
        button3.pack()


class future(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="FUTURE TENSE", font=BIG_FONT)
        label.pack(pady=10, padx=10)

        label = tk.Label(self,
                         text="SIMPLE FUTURE TENSE:-\n The Simple Future Tense is used to talk about things which\n we cannot control or to predict what may happen. \n It expresses the future as fact.\n EXAMPLE:-\n It will be Christmas in a week.\n Structure:- WILL/SHALL + VERB",
                         font=SMALL_FONT)
        label.pack(pady=12, padx=5)
        label = tk.Label(self,
                         text="FUTURE CONTINOUS TENSE:-\n It resembles the work which is continouing to till future is called future continous tense.\nEXAMPLE:-I shall be going to the market tomorrow.\n Structure:- Subject + will be/shall be + V1 + ing + Object",
                         font=SMALL_FONT)
        label.pack(pady=14, padx=5)
        label = tk.Label(self,
                         text="FUTURE PERFECT TENSE:-\n The work or thing which is going to happen in future till has time limit\n EXAMPLE:-I shall have prepared the notes by tomorrow morning\n Structure:- Subject + will have/shall have + V3 + Object",
                         font=SMALL_FONT)
        label.pack(pady=16, padx=5)
        label = tk.Label(self,
                         text="FUTURE PERFECT CONTINOUS TENSE:-\n The thing or an event which going to continue in future is called future perfect continous tense.\n EXAMPLE:-She will have been working here since 2015 \n Structure:- Subject + will have been + V1 + ing + Object",
                         font=SMALL_FONT)
        label.pack(pady=18, padx=5)

        button3 = tk.Button(self, text="Back to chapters",
                            command=lambda: controller.show_frame(english))
        button3.pack()

        button3 = tk.Button(self, text="Back to tenses",
                            command=lambda: controller.show_frame(tense))
        button3.pack()

        button3 = tk.Button(self, text="Back to subjects",
                            command=lambda: controller.show_frame(subjectPage))
        button3.pack()


app = python()
app.mainloop()
