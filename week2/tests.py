def vowel_counter(s):
    vowel_count = 0
    for char in s:
        if char == "a" or char == "e" or char == "i" \
            or char == "o" or char == "u":
            vowel_count += 1
    return vowel_count

def bob_counter(s):
    bob_count = 0
    for index in range(len(s)):
        if s[index:index+3]=="bob":
            bob_count += 1
    return bob_count
    
def item_order(order):
    salad_count = 0
    hamburger_count = 0
    water_count = 0
    order_list = order.split(" ")
    for item in order_list:
        if item == "salad":
            salad_count += 1
        elif item == "hamburger":
            hamburger_count += 1
        else:
            water_count += 1
    return "salad:%s hamburger:%s water:%s" % (
        salad_count, hamburger_count, water_count)






import unittest
class TestProblemSet1(unittest.TestCase):
    def test_counts_vowels_correctly(self):
        self.assertEqual(vowel_counter("some random string of words with vowels and consanants."),14)
        
    def test_counts_bobs_correctly(self):
        self.assertEqual(bob_counter('azcbobobegghakl'), 2)
        
    def test_counts_order_items_correctly(self):
        self.assertEqual(
            item_order("salad water hamburger salad hamburger"),
            "salad:2 hamburger:2 water:1"
        )
if __name__ == "__main__":
    unittest.main()
    
    
