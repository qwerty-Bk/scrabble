from random import sample


class Bag:
    bag = [
        'а', 'а', 'а', 'а', 'а', 'а', 'а', 'а', 'а',
        'б', 'б', 'в', 'в', 'в', 'в', 'г', 'г',
        'д', 'д', 'д', 'е', 'е', 'е', 'е', 'е', 'е', 'е', 'е',
        'ж', 'ж', 'з', 'з', 'и', 'и', 'и', 'и', 'и', 'и', 'и',
        'й', 'к', 'к', 'к', 'к', 'л', 'л', 'л', 'л', 'м', 'м', 'м',
        'н', 'н', 'н', 'н', 'н', 'н',
        'о', 'о', 'о', 'о', 'о', 'о', 'о', 'о', 'о',
        'п', 'п', 'п', 'р', 'р', 'р', 'р', 'р', 'р', 'с', 'с', 'с', 'с', 'с',
        'т', 'т', 'т', 'т', 'т', 'т', 'у', 'у', 'у', 'ф', 'х', 'ц', 'ч', 'ш',
        'щ', 'ы', 'ы', 'ь', 'ь', 'э', 'ю', 'я', 'я', 'ё', 'ё'
    ]

    def __init__(self, bag=None):
        if bag is not None:
            self.bag = bag

    def get(self, num):
        s = sample(self.bag, min(num, len(self.bag))) if num > 0 else []
        for i in s: self.bag.remove(i)
        return s

    def add(self, seq):
        num = len(seq)
        self.bag += seq
        return num

    def __bool__(self):
        return bool(self.bag)

    def __len__(self):
        return len(self.bag)
