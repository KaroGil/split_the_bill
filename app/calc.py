class Convert:
    def convert_bill_share(self, total, your_share, money_from_bank):
        '''
        convert bill share to the amount you owe
        '''
        if total == 0:
            return 0
        
        p = your_share / total
        amount = p * money_from_bank

        return amount


    def split_several_bills(self, total_list, share_list, bank_statement_list):
        '''
        convert a list of bill shares into the total amount you owe
        '''
        total_amount = 0
        l = len(total_list)
        if not (l == len(share_list) == len(bank_statement_list)):
            return 0
        for i in range(l):
            total_amount += self.convert_bill_share(total_list[i], share_list[i], bank_statement_list[i])

        return total_amount
