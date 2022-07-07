class BoardingPass:

    def __init__(self, chars, seat_rows=127, seat_cols=7, n_row_bisections=7):
        self.row_bisections = chars[0:n_row_bisections]
        self.col_bisections = chars[n_row_bisections:]
        self.seat_rows = seat_rows
        self.seat_cols = seat_cols
    
    def resolve_row(self, bisection_ind=0, min_row=0, max_row=127):
        if min_row - max_row == 0 :
            return min_row
        elif bisection_ind == len(self.row_bisections):
            print(f"ERROR: this should not have more than one row, min row is {min_row} and max is {max_row}")
            return min_row
        
        direction = self.row_bisections[bisection_ind]
        mid = (min_row + max_row) // 2
        if direction == "F":
            return self.resolve_row(bisection_ind + 1, min_row = min_row, max_row = mid)
        elif direction == "B":
            return self.resolve_row(bisection_ind + 1, min_row = mid + 1, max_row = max_row)
        else:
            print(f"ERROR this should not happen, values should only be F or B, but current val is {direction}")
        
    def resolve_col(self, bisection_ind=0, min_col=0, max_col=7):
        if min_col - max_col == 0 :
            return min_col
        elif bisection_ind == len(self.col_bisections):
            print(f"ERROR: this should not have more than one col, min col is {min_col} and max is {max_col}")
            return min_col
        
        direction = self.col_bisections[bisection_ind]
        mid = (min_col + max_col) // 2
        if direction == "L":
            return self.resolve_col(bisection_ind + 1, min_col = min_col, max_col = mid)
        elif direction == "R":
            return self.resolve_col(bisection_ind + 1, min_col = mid + 1, max_col = max_col)
        else:
            print(f"ERROR this should not happen, values should only be F or B, but current val is {direction}")

    def calc_seat_id(self, row_multiplier=8):
        row = self.resolve_row(bisection_ind=0,min_row=0,max_row=127)
        col = self.resolve_col(bisection_ind=0,min_col=0,max_col=7)
        return (row*row_multiplier) + col
        
