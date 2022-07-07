from BoardingPass1 import BoardingPass

max_seat_id = 0
with open("./boarding_passes.txt") as boarding_passes:
    for boarding_pass in boarding_passes:
        boarding_pass_object = BoardingPass(chars=boarding_pass)
        seat_id = boarding_pass_object.calc_seat_id()
        print(seat_id)
        max_seat_id = max(max_seat_id, seat_id)
print(f"max id is {max_seat_id}")