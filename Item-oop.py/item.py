from abc import ABC , abstractmethod
# Item
class Item (ABC):
    num_of_items = 1
    def __init__(self,name,year,pric,publi,lang,nop):
        self.gsname = name
        self.gsyear = year
        self.gsprice = pric
        self.gspublisher = publi
        self.gslanguage = lang
        self.gsnum_of_pages = nop

    def generate_id(self):
        id = (f"ID: {self.gsname}{self.gsyear}")
        return id
    
    def convert_pages_to_sheet(self):
        self.gsnum_of_sheet = self.gsnum_of_pages / 2
        return self.gsnum_of_sheet
    

    @classmethod
    def increase_item(cls):
        cls.num_of_items += 1
        return cls.num_of_items

    def __str__(self):
        return self.show_full_info()
    
    # Name (Nabayyad khali bashad)
    @property
    def gsname(self):
        return self.name
    @gsname.setter
    def gsname(self,valu):
        if len(valu) == 0:
            raise ValueError ("Name Cannot be empoty!")
        else:
            self.name = valu
    
    # Year (Bayad motabar bashad)
    @property
    def gsyear(self):

        return self.year
    @gsyear.setter
    def gsyear(self,valu):
        if 1300 < valu < 1404: # Az 1300 va 1404 astefade kardam chon rarikh ro shamsi zadim
            self.year = valu
        else:
            raise ValueError ("Invalid Year (Should not be after 2025 and befor 1950)")

    # Price (Nabayad manfi bashad)
    @property
    def gsprice(self):
        return self.price
    @gsprice.setter
    def gsprice(self,valu):
        if valu >= 0:
            self.price = valu
        else:
            raise ValueError ("Price Cannot Be Negative!")

    # Publisher (Nabayad khali bashad)
    @property
    def gspublisher(self):
        return self.publi
    @gspublisher.setter
    def gspublisher(self,valu):
        if len(valu) != 0:
            self.publi = valu
        else:
            raise ValueError ("Publisher Cannot be empoty!")
        
    # Language (Nabayad khali bashad)
    @property
    def gslanguage(self):
        return self.lang
    @gslanguage.setter
    def gslanguage(self,valu):
        if len(valu) != 0:
            self.lang = valu
        else:
            raise ValueError ("Language Cannot be empoty!")
        
    # Num Of Page (Nabayad manfi bashad)
    @property
    def gsnum_of_pages(self):
        return self.nop
    @gsnum_of_pages.setter
    def gsnum_of_pages(self,valu):
        if valu >=0 :
            self.nop = valu
        else:
            raise ValueError ("Num Of Page Cannot Be Negative!")

    # Dunder Methods 
    def __str__(self):
        return f"{self.name} ({self.year})"
    
    def __len__(self):
        return self.nop

    def __sub__(self, other):
        if isinstance(other, Item):
            return self.year - other.year
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        return NotImplemented
    
    def __del__(self):
        Item.num_of_items -= 1
        print(f"Item deleted! Remaining items: {Item.num_of_items}")



class Full_info(Item):
    def show_full_info(self):
        return (f"""Name: {self.name}
Year: {self.year}
Price: {self.price}
Publisher: {self.publi}
language: {self.lang}
Num Of Page: {self.nop}""")

# Object
print("\033[31m--- Item Test ---\033[0m")
i1 = Full_info("Heart",1403,1800000,"Negar","Persian",160)
print(i1.generate_id())
print("Half Pages:",i1.convert_pages_to_sheet())
print(f"Num Of Item: {i1.increase_item()}")
print(i1.show_full_info())

# TEST KHALI NABODAN NAME
# i2 = Full_info("",1400,2800000,"Nor","Persian",122)
# print(i2.generate_id())
# print(i2.convert_pages_to_sheet())
# print(f"Num Of Item: {i2.increase_item()}")
# print(i2.show_full_info())

# TEST MOTABAR BODAN YEAR
# i3 = Full_info("fly",0,1300000,"Nor","Persian",132)
# print(i3.generate_id())
# print(i3.convert_pages_to_sheet())
# print(f"Num Of Item: {i3.increase_item()}")
# print(i3.show_full_info())

# TEST MANFI NABODAN GHYMAT
# i4 = Full_info("Gang",1387,-1800000,"lord","Persian",120)
# print(i4.generate_id())
# print(i4.convert_pages_to_sheet())
# print(f"Num Of Item: {i4.increase_item()}")
# print(i4.show_full_info())

# TEST KHALI NABODAN NASHER
# i5 = Full_info("Gang2",1391,2800000,"","Persian",120)
# print(i5.generate_id())
# print(i5.convert_pages_to_sheet())
# print(f"Num Of Item: {i5.increase_item()}")
# print(i5.show_full_info())

# TEST KHALI NABODAN LANGUAGE
# i6 = Full_info("Momo",1377,1500000,"Moze","",175)
# print(i6.generate_id())
# print(i6.convert_pages_to_sheet())
# print(f"Num Of Item: {i6.increase_item()}")
# print(i6.show_full_info())

# TEST (BARESI MOSBAT BODAN PAGE)
# i7 = Full_info("Momo",1377,1500000,"Moze","Persian",-55)
# print(i7.generate_id())
# print(i7.convert_pages_to_sheet())
# print(f"Num Of Item: {i7.increase_item()}")
# print(i7.show_full_info())

# Dunder Methods
print("\033[95mDunder Methods:\033[0m")
i = Full_info("Test", 1395, 2000000, "Nor", "Persian", 120)
i1 = Full_info("Heart", 1403, 1800000, "Negar", "Persian", 160)

print("Restore name and year of Publication:",str(i1))          # Heart (1403)
print("Restore page Count:",len(i1))                            # 160
print("Publication year Difference:",i1 - i)                     # 8  (Akhtelaf sal)
print("Sum of Prices:",i1 + i)                                  # 3800000  (Jam ghaymat)
# del i                                                         # Hazf shay ==> kam shodan item ha


# Book
class Book(Item):
    num_of_books = 0
    increase_book = 0
    def __init__(self, name, year, price, publi, lang, nop, an, hdv, hav, ct, sub, edi):
        super().__init__(name, year, price, publi, lang, nop)
        self.gsauthor_name = an
        self.gshas_digital_version = hdv
        self.gshas_audio_version = hav
        self.gscover_type = ct
        self.gssubject = sub
        self.gsedition = edi

        Book.num_of_books += 1


    valid_digital = ["JPEG", "JPG", "PNG", "GIF", "BMP", "TIFF", "WEBP", "SVG"]
    def set_digital_version_format(self,valu):
        if valu.upper() in self.valid_digital:
            self.gshas_digital_version = valu
        else:
            raise ValueError ("The digital version must be (JPEG or JPG or PNG or GIF or BMP or TIFF or WEBP or SVG) ")


    valid_audio = ["MP3", "WAV", "ALAC", "FLAC", "AAC"]
    def set_audio_version_format(self,valu):
        if valu.upper() in self.valid_audio:
            self.gshas_audio_version = valu
        else:
            raise ValueError ("The audio version must be (MP3 or WAV or ALAC or FLAC or ALAC or AAC) ")

    def full_info(self):
        return (f""" Name: {Item.gsname}
Author Name: {self.an}
Publisher: {self.gspublisher}
Year: {self.gsyear}
Language: {self.gslanguage}""")
    
    @classmethod
    def increase_book(cls):
        cls.num_of_books += 1
        return cls.num_of_books

    # Author_Name (Nabayad khali bashad)
    @property
    def gsauthor_name (self):
        return self.an
    @gsauthor_name.setter
    def gsauthor_name(self,valu):
        if len(valu) != 0:
            self.an = valu
        else:
            raise ValueError ("Author Name Cannot be empoty!")

    # Has_Digital_Version (Tabdil be boolean)
    @property
    def gshas_digital_version(self):
        return self.hdv
    @gshas_digital_version.setter
    def gshas_digital_version(self,valu):
        if valu.upper() in self.valid_digital:
            self.hdv = True
            self.set_digital_version_format = valu.upper()
        else:
            save_d = self.hdv = False
            raise ValueError ("The digital version must be (JPEG or JPG or PNG or GIF or BMP or TIFF or WEBP or SVG) ")


    # Has_Audio_Version (Tabdil be boolean) T , F
    @property
    def gshas_audio_version(self):
        return self.hav
    @gshas_audio_version.setter
    def gshas_audio_version(self,valu):
        if valu.upper() in self.valid_audio:
            save_a = self.hav = True
            self.set_audio_version_format = valu.upper()
            return save_a

        else:
            save_a = self.hav = False
            raise ValueError ("The audio version must be (MP3 or WAV or ALAC or FLAC or ALAC or AAC)")

    # Cover Type (Nabayad khali bashad)
    @property
    def gscover_type(self):
        return self.ct
    @gscover_type.setter
    def gscover_type(self,valu):
        if len(valu) != 0:
            self.ct = valu
        else:
            raise ValueError ("Cover Type Cannot be empoty!")

    # Subject (Nabayad khali bashad)
    @property
    def gssubject(self):
        return self.sub
    @gssubject.setter
    def gssubject(self,valu):
        if len(valu) != 0:
            self.sub = valu
        else:
            raise ValueError ("Subject Cannot be empoty!")

    # Edition (Nabayad khali bashad)
    @property
    def gsedition(self):
        return self.edi
    @gsedition.setter
    def gsedition(self,valu):
        if len(valu) != 0:
            self.edi = valu
        else:
            raise ValueError ("Edition Cannot be empoty!")

    # Dunder Methods 
    def __str__(self):
        return (f"{self.gsauthor_name} {self.gsname}")

    def __len__(self):
        return self.gsnum_of_pages

    def __sub__(self, other):
        if isinstance(other, Book):
            return self.gsnum_of_pages - other.gsnum_of_pages
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Book):
            return self.gsprice + other.gsprice
        return NotImplemented

    def __del__(self):
        Book.num_of_books -= 1
        print(f"Book deleted! Remaining books: {Book.num_of_books}")

# Object (b1 = Book("Ahmadi", "JPEG", "aac", "Hard", "Novel", "2nd", 10))
# (valid_digital = ["JPEG", "JPG", "PNG", "GIF", "BMP", "TIFF", "WEBP", "SVG"])
# (valid_audio = ["MP3", "WAV", "ALAC", "FLAC", "AAC"])
print("\n\033[31m--- Book Tests ---\033[0m")
b1 = Book("AI Basics", 1402, 200000, "Negar", "Persian", 300,
           "Ahmadi", "jpeg", "aac", "Hard", "Novel", "2nd")
print("Author:", b1.gsauthor_name)
print("Digital Version:", b1.gshas_digital_version,"--->","Format:",b1.set_digital_version_format)
print("Audio Version:", b1.gshas_audio_version,"--->","Format:",b1.set_audio_version_format)
print("Cover:", b1.gscover_type)
print("Subject:", b1.gssubject)
print("Edition:", b1.gsedition)
print("Num Of Books: ",b1.num_of_books)

# Author Name TEST
# b2 = Book("AI Basics", 1402, 200000, "Negar", "Persian", 300,
#            "", "jpeg", "aac", "Hard", "Novel", "2nd")
# print("Author:", b2.gsauthor_name)
# print("Digital Version:", b2.gshas_digital_version,"--->","Format:",b2.set_digital_version_format)
# print("Audio Version:", b2.gshas_audio_version,"--->","Format:",b2.set_audio_version_format)
# print("Cover:", b2.gscover_type)
# print("Subject:", b2.gssubject)
# print("Edition:", b2.gsedition)
# print("Num Of Books: ",b2.num_of_books)

# Digital TEST (valid_digital = ["JPEG", "JPG", "PNG", "GIF", "BMP", "TIFF", "WEBP", "SVG"])
# b3 = Book("AI Basics", 1402, 200000, "Negar", "Persian", 300,
#            "Ahmadi", "txt", "aac", "Hard", "Novel", "2nd")
# print("Author:", b3.gsauthor_name)
# print("Digital Version:", b3.gshas_digital_version,"--->","Format:",b3.set_digital_version_format)
# print("Audio Version:", b3.gshas_audio_version,"--->","Format:",b3.set_audio_version_format)
# print("Cover:", b3.gscover_type)
# print("Subject:", b3.gssubject)
# print("Edition:", b3.gsedition)
# print("Num Of Books: ",b3.num_of_books)

# Audio TEST (valid_audio = ["MP3", "WAV", "ALAC", "FLAC", "AAC"])
# b4 = Book("AI Basics", 1402, 200000, "Negar", "Persian", 300,
#            "Ahmadi", "jpeg", "png", "Hard", "Novel", "2nd")
# print("Author:", b4.gsauthor_name)
# print("Digital Version:", b4.gshas_digital_version,"--->","Format:",b4.set_digital_version_format)
# print("Audio Version:", b4.gshas_audio_version,"--->","Format:",b4.set_audio_version_format)
# print("Cover:", b4.gscover_type)
# print("Subject:", b4.gssubject)
# print("Edition:", b4.gsedition)
# print("Num Of Books: ",b4.num_of_books)

# Cover_type TEST
# b5 = Book("AI Basics", 1402, 200000, "Negar", "Persian", 300,
#            "Ahmadi", "jpeg", "aac", "", "Novel", "2nd")
# print("Author:", b5.gsauthor_name)
# print("Digital Version:", b5.gshas_digital_version,"--->","Format:",b5.set_digital_version_format)
# print("Audio Version:", b5.gshas_audio_version,"--->","Format:",b5.set_audio_version_format)
# print("Cover:", b5.gscover_type)
# print("Subject:", b5.gssubject)
# print("Edition:", b5.gsedition)
# print("Num Of Books: ",b5.num_of_books)

# Subject TEST
# b6 = Book("AI Basics", 1402, 200000, "Negar", "Persian", 300,
#            "Ahmadi", "jpeg", "aac", "Hard", "", "2nd")
# print("Author:", b6.gsauthor_name)
# print("Digital Version:", b6.gshas_digital_version,"--->","Format:",b6.set_digital_version_format)
# print("Audio Version:", b6.gshas_audio_version,"--->","Format:",b6.set_audio_version_format)
# print("Cover:", b6.gscover_type)
# print("Subject:", b6.gssubject)
# print("Edition:", b6.gsedition)
# print("Num Of Books: ",b6.num_of_books)

# Edition TEST
# b7 = Book("AI Basics", 1402, 200000, "Negar", "Persian", 300,
#            "Ahmadi", "jpeg", "aac", "Hard", "Novel", "")
# print("Author:", b7.gsauthor_name)
# print("Digital Version:", b7.gshas_digital_version,"--->","Format:",b7.set_digital_version_format)
# print("Audio Version:", b7.gshas_audio_version,"--->","Format:",b7.set_audio_version_format)
# print("Cover:", b7.gscover_type)
# print("Subject:", b7.gssubject)
# print("Edition:", b7.gsedition)
# print("Num Of Books: ",b7.num_of_books)

# Dunder Methods
print("\033[95mDunder Methods:\033[0m")
b = Book("TEST", 1402, 200000, "Negar", "Persian", 300,
           "Ahmadi", "jpeg", "aac", "Hard", "Novel", "2nd")
b1 = Book("AI Basics", 1400, 180000, "Negar", "Persian", 100,
           "Ahmadi", "jpeg", "aac", "Hard", "Novel", "2nd")
print("Author Name + Book Name:",str(b1))      # Test by Ahmadi
print("Number Of Page:",len(b1))                # 300 (Tedad safahat)
print("Different Pages:",b - b1)                 # 150 (Tafavot safahat)
print("Total Pages:",b1 + b)                      # 380000 (Jam ghaymat ha)
# del b1                                            # Book deleted! Remaining books: 1


# Magazine
class Magazine(Book):
    num_of_magazine = 1
    def __init__(self, name, year, price, publi, lang, nop, an, hdv, hav, ct, sub, edi,pp,edit,mn):
        super().__init__(name, year, price, publi, lang, nop, an, hdv, hav, ct, sub, edi)
        self.gspublication_period = pp
        self.gseditor = edit
        self.gsmag_num = mn

    def calculate_reading_time(self,read_speed):
        return self.gsnum_of_pages / read_speed
    @staticmethod
    def preprocess_string_for_object(self):
        return self.split("--")
    
    @classmethod
    def increase_magazine(self):
        self.num_of_magazine +=1
        return self.num_of_magazine

    def full_info(self):
       return (f"""publication_period: {self.pp}
Editor: {self.edit}
mag_num: {self.mn}
num_of_magazine: {self.num_of_magazine}""")
        
    # publication_period (Nabayad khali bashad)
    @property
    def gspublication_period(self):
        return self.pp
    @gspublication_period.setter
    def gspublication_period(self,valu):
        if len(valu) != 0:
            self.pp = valu
        else:
            raise ValueError ("Publication Period Cannot be empoty!")

    # Editor (Nabayad khali bashad)
    @property
    def gseditor(self):
        return self.edit
    @gseditor.setter
    def gseditor(self,valu):
        if len(valu) != 0:
            self.edit = valu
        else:
            raise ValueError ("Editor Cannot be empoty!")
        
    # Mag Num (Nabayad khali bashad)
    @property
    def gsmag_num(self):
        return self.mn
    @gsmag_num.setter
    def gsmag_num(self,valu):
        if len(valu) != 0:
            self.mn = valu
        else:
            raise ValueError ("Mag Num Cannot be empoty!")
        
    # Dunder Methods 
    def __str__(self):
        return (f"{self.name} {self.gsmag_num}")

    def __len__(self):
        return self.gsnum_of_pages

    def __sub__(self, other):
        if isinstance(other, Magazine):
            return int(self.gsmag_num) - int(other.gsmag_num)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Magazine):
            return self.gsprice + other.gsprice
        return NotImplemented

    def __del__(self):
        Magazine.num_of_magazine -= 1
        print(f"Magazin deleted! Remaining books: {Magazine.num_of_magazine}")

print("\n\033[31m--- Magazine TESt ---\033[0m")
b1 = Magazine("AI Basics", 1402, 200000, "Negar", "Persian", 300,
           "Ahmadi", "jpeg", "aac", "Hard", "Novel", "2nd","Mounth","Madhi","1")
print("Page/min:", b1.calculate_reading_time(30))
print("Preprocess String:", b1.preprocess_string_for_object("Python--word"))
print("Increase Magazine:", b1.increase_magazine())
print("Full Info:", b1.full_info())
print("Release rope:",b1.gspublication_period)
print("Name of the editor:",b1.gseditor)
print("Mag Number:",b1.gsmag_num)

# b2 = Magazine("AI Basics", 1402, 200000, "Negar", "Persian", 300,
#            "Ahmadi", "jpeg", "aac", "Hard", "Novel", "2nd","","Madhi","1")
# print("Page/min:", b2.calculate_reading_time(30))
# print("Preprocess String:", b2.preprocess_string_for_object("Python--word"))
# print("Increase Magazine:", b2.increase_magazine())
# print("Full Info:", b2.full_info())
# print("Release rope:",b2.gspublication_period)
# print("Name of the editor:",b2.gseditor)
# print("Mag Number:",b2.gsmag_num)

# Editor TEST
# b3 = Magazine("AI Basics", 1402, 200000, "Negar", "Persian", 300,
#            "Ahmadi", "jpeg", "aac", "Hard", "Novel", "2nd","Week","","1")
# print("Page/min:", b3.calculate_reading_time(30))
# print("Preprocess String:", b3.preprocess_string_for_object("Python--word"))
# print("Increase Magazine:", b3.increase_magazine())
# print("Full Info:", b3.full_info())
# print("Release rope:",b3.gspublication_period)
# print("Name of the editor:",b3.gseditor)
# print("Mag Number:",b3.gsmag_num)

# Mag Num TEST
# b4 = Magazine("AI Basics", 1402, 200000, "Negar", "Persian", 300,
#            "Ahmadi", "jpeg", "aac", "Hard", "Novel", "2nd","Week","Ali","")
# print("Page/min:", b4.calculate_reading_time(30))
# print("Preprocess String:", b4.preprocess_string_for_object("Python--word"))
# print("Increase Magazine:", b4.increase_magazine())
# print("Full Info:", b4.full_info())
# print("Release rope:",b4.gspublication_period)
# print("Name of the editor:",b4.gseditor)
# print("Mag Number:",b4.gsmag_num)

# Dunder Methods
print("\033[95mDunder Methods:\033[0m")
b = Magazine("Test", 1402, 200000, "Negar", "Persian", 100,
           "Ahmadi", "jpeg", "aac", "Hard", "Novel", "2nd","Mounth","Madhi","1")
b1 = Magazine("AI Basics", 1402, 300000, "Negar", "Persian", 200,
           "Ahmadi", "jpeg", "aac", "Hard", "Novel", "2nd","Mounth","Madhi","1")
print("Name + Mag Num:",str(b1))                # Test by Ahmadi
print("Number Of Page:",len(b1))                # 200 (Tedad safahat)
print("Different Pages:",b - b1)
print("Price:",b1 + b)                          # 500000 (Jam ghaymat ha)
# del b1                                        # Magazin deleted! Remaining magazin: 1


# ResearchJournal
class ResearchJournal(Magazine):
    citations_count = 0 
    def __init__(self, name, year, pric, publi, lang, nop,im,iss,scop,rt,sd,ar,eb):
        Item.__init__(self,name, year, pric, publi, lang, nop)
        self.impact_factor = im
        self.issn = iss
        self.scope = scop
        self.review_type = rt
        self.submission_deadline = sd
        self.acceptance_rate = ar
        self.eb = eb

    def add_editor(self, name):
        self.editorial_board.append(name)

    def get_editors(self):
        return self.editorial_board

    def calculate_h_index(self):
        from math import sqrt
        return int(sqrt(ResearchJournal.citations_count / 10))

    def acceptance_probability(self):
        if isinstance(self.acceptance_rate, str) and self.acceptance_rate.endswith("%"):
            return float(self.acceptance_rate.strip("%")) / 100
        return float(self.acceptance_rate)

    def full_info(self):
        return (f"""Journal ISSN: {self.issn}
Impact Factor: {self.impact_factor}
Scope: {self.scope}
Review Type: {self.review_type}
Submission Deadline: {self.submission_deadline}
Acceptance Rate: {self.acceptance_rate}
Editorial Board: {', '.join(self.editorial_board)}
Total Citations (Class): {ResearchJournal.citations_count}
Total Magazines (Class): {ResearchJournal.num_of_magazine}""")

    @classmethod
    def increase_magazine(cls):
        cls.magazine_count += 1
    

    # impact_factor (Nabayad manfi bashad)
    @property
    def impact_factor(self):
        return self.im
    @impact_factor.setter
    def impact_factor(self,valu):
        if valu >= 0:
            self.im = valu
        else:
            raise ValueError ("impact factor Cannot be Negetive!")

    # issn (Nabayad khali bashad)
    @property
    def issn(self):
        return self.iss
    @issn.setter
    def issn(self,valu):
        if len(valu) != 0:
            self.iss = valu
        else:
            raise ValueError ("Issn Cannot be empoty!")
        
    # scope (Nabayad khali bashad)
    @property
    def scope(self):
        return self.scop
    @scope.setter
    def scope(self,valu):
        if len(valu) != 0:
            self.scop = valu
        else:
            raise ValueError ("Scope Cannot be empoty!")
    
    # review_type (Nabayad khali bashad)
    @property
    def review_type(self):
        return self.rt
    @review_type.setter
    def review_type(self,valu):
        if len(valu) != 0:
            self.rt = valu
        else:
            raise ValueError ("Review Type Cannot be empoty!")
        
    # submission_deadline (Nabayad khali bashad)
    @property
    def submission_deadline(self):
        return self.sd
    @submission_deadline.setter
    def submission_deadline(self,valu):
        if len(valu) != 0:
            self.sd = valu
        else:
            raise ValueError ("Submission Deadline Type Cannot be empoty!")
        
    # acceptance_rate (Bin 0 ta 100)
    @property
    def acceptance_rate(self):
        return self.ar
    @acceptance_rate.setter
    def acceptance_rate(self,valu):
        if 0 <= valu <=100 :
            self.ar = valu
        else:
            raise ValueError ("Acceptance Rate (0,100)")

    # editorial_board (Bin 0 ta 100)
    @property
    def editorial_board(self):
        return self.eb
    
    
    def __str__(self):
        return (f"ResearchJournal: {self.name} (ISSN: {self.issn})")

    def __len__(self):
        return self.gsnum_of_pages   # تعداد صفحات

    def __sub__(self, other):
        if isinstance(other, ResearchJournal):
            return self.impact_factor - other.impact_factor
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, ResearchJournal):
            return self.gsprice + other.gsprice
        return NotImplemented

    def __del__(self):
        ResearchJournal.num_of_magazine -= 1
        ResearchJournal.citations_count -= 1
        print(f"ResearchJournal deleted! Remaining journals: {ResearchJournal.num_of_magazine}, "
              f"Citations: {ResearchJournal.citations_count}")
    

print("---\n\033[31mResearch Journal Test\033[0m---")
rj1 = ResearchJournal("AI Basics", 1402, 200000, "Negar", "Persian", 300,
                      5.6, "1234-5678", "AI", "Peer-review",
                      "2025-12-01", 35, ["Dr. Ali", "Dr. Sara"])
rj2 = ResearchJournal("ML World", 1401, 250000, "Springer", "English", 250,
                      7.2, "8765-4321", "ML", "Blind-review",
                      "2025-06-01", 40, ["Dr. Reza", "Dr. Neda"])
print(rj1.full_info())  
print(str(rj1))
print("Pages:", len(rj1))
print("Impact Factor Diff:", rj2 - rj1)  
print("Total Price:", rj1 + rj2)
rj1.add_editor("Dr. Reza")
print("Updated Editors:", rj1.get_editors())
ResearchJournal.citations_count = 500
print("h-index:", rj1.calculate_h_index())
print("Acceptance Probability:", rj1.acceptance_probability())
# del rj2