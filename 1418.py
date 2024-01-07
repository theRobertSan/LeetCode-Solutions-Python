from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tableDishFreq = {}
        dishes, tables = set(), set()

        for _, table, dish in orders:
            if table not in tableDishFreq:
                tableDishFreq[table] = {}

            if dish not in tableDishFreq[table]:
                tableDishFreq[table][dish] = 0

            tableDishFreq[table][dish] += 1

            dishes.add(dish)
            tables.add(int(table))

        dishes = sorted(dishes)
        tables = sorted(tables)

        output = [["Table"] + dishes]

        for table in tables:
            tableStr = str(table)
            row = [tableStr]

            for dish in dishes:
                quantity = 0
                if dish in tableDishFreq[tableStr]:
                    quantity = tableDishFreq[tableStr][dish]

                row.append(str(quantity))

            output.append(row)

        return output
