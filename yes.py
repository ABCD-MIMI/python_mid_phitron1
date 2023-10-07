class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self._hall_no = hall_no

    def entry_show(self, id: str, movie_name: str, time: str):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        seating_arrangement = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seating_arrangement

    def view_show_list(self):
        for id, movie_name, time in self.__show_list:
            print(f"Hall No: {self._hall_no}, Show ID: {id}, Movie: {movie_name}, Time: {time}")

    def book_seats(self, id: str, seats_to_book: list):
        if id not in self.__seats:
            print("No show exists with given ID.")
            return
        for seat in seats_to_book:
            row, col = seat
            if 0 <= row < self.__rows and 0 <= col < self.__cols:
                if self.__seats[id][row][col] == 0:
                    self.__seats[id][row][col] = 1
                else:
                    print(f"Seat {seat} is already booked.")
                    return
            else:
                print(f"Invalid seat: {seat}.")
                return
        print(f"Seats {seats_to_book} booked successfully for show id {id}")

    def view_available_seats(self, id):
        if id not in self.__seats:
            print("Show doesn't exist.")
            return
        available_seats = [(i, j) for i in range(self.__rows) for j in range(self.__cols) if self.__seats[id][i][j] == 0]
        if available_seats:
            print("Available seats:")
            for seat in available_seats:
                print(f"seat: {seat}")
        else:
            print("No seats available.")


class Star_Cinema(Hall):
    __hall_list = []

    def __init__(self, rows, cols, hall_no):
        super().__init__(rows, cols, hall_no)
        self.__entry_hall(self)

    @classmethod
    def __entry_hall(cls, hall_obj):
        cls.__hall_list.append(hall_obj)

    @classmethod
    def view_all_shows(cls):
        for hall in cls.__hall_list:
            hall.view_show_list()


if __name__ == "__main__":
    cinema1 = Star_Cinema(7, 8, 1)
    cinema1.entry_show("111", "Jauyan Maji", "25/10/23 11:00 AM")
    cinema2 = Star_Cinema(15, 12, 2)
    cinema2.entry_show("333", "Sujon Maji", "25/10/23 2:00 PM")

    while True:
        print("\nPlease choose an option:")
        print("1. View available shows")
        print("2. View available seats in a show")
        print("3. Book tickets for a show")
        print("4. Exit")

        option = int(input("Enter option: "))

        if option == 1:
            Star_Cinema.view_all_shows()
        elif option == 2:
            show_id = input("Enter the ID: ")
            hall_no = int(input("Enter hall number: "))
            if hall_no == 1:
                cinema1.view_available_seats(show_id)
            elif hall_no == 2:
                cinema2.view_available_seats(show_id)
            else:
                    print("Invalid Hall Number.")
        elif option == 3:
            show_id = input("Enter the ID : ")
            hall_no = int(input("Enter hall number: "))
            num_tickets = int(input("Number of tickets?: "))
            seat_coords = []
            for _ in range(num_tickets):
                row = int(input("Enter the row: "))
                col = int(input("Enter the column: "))
                seat_coords.append((row, col))

            if hall_no == 1:
                cinema1.book_seats(show_id, seat_coords)
            elif hall_no == 2:
                cinema2.book_seats(show_id, seat_coords)
            else:
                print("Invalid Hall Number.")