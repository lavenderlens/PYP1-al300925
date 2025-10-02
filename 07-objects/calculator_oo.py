class Calculator:
    def __init__(this):
        this.total = 0
    
    def add(this, num):
        this.total += num
    def sub(this, num):
        this.total -= num
    def mul(this, num):
        this.total *= num
    def div(this, num):
        if num != 0:
            this.total /= num

    def equals(this):
        temp_total = this.total
        this.total = 0
        return temp_total
