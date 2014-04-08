from oceangui.events import EventManager, INotifyable

class ZombieAttack (INotifyable):
    def set_unit(self, unit, x_coord, y_coord):
        """
        Sets the unit to the desired x and y coordnates for the event
        """
        self.x = x_coord
        self.y = y_coord
        # Draw Zombie
        pass

    def notify (self, event):
        # Check the event signal and run a certain action with its data.
        if event.signal == "clicked":
           print "Something was clicked!"
        elif event.signal == "move":
           # Assuming that the event.data contains a coordinate tuple.
           self.move (event.data)

class SurvivorFound (INotifyable):
    def set_unit(self, unit, x_coord, y_coord):
        """
        Sets the unit to the desired x and y coordnates for the event
        """
        self.x = x_coord
        self.y = y_coord
        # Draw Zombie
        pass

    def notify (self, event):
        # Check the event signal and run a certain action with its data.
        if event.signal == "clicked":
           print "Something was clicked!"
        elif event.signal == "move":
           # Assuming that the event.data contains a coordinate tuple.
           self.move (event.data)

class WeaponFound (INotifyable):
    def set_item(self, item, x_coord, y_coord):
        """
        Sets the unit to the desired x and y coordnates for the event
        """
        self.x = x_coord
        self.y = y_coord
        # Draw Zombie
        pass

    def notify (self, event):
        # Check the event signal and run a certain action with its data.
        if event.signal == "clicked":
           print "Something was clicked!"
        elif event.signal == "move":
           # Assuming that the event.data contains a coordinate tuple.
           self.move (event.data)

class FoodFound (INotifyable):
    def set_item(self, item, x_coord, y_coord):
        """
        Sets the unit to the desired x and y coordnates for the event
        """
        self.x = x_coord
        self.y = y_coord
        # Draw Zombie
        pass

    def notify (self, event):
        # Check the event signal and run a certain action with its data.
        if event.signal == "clicked":
           print "Something was clicked!"
        elif event.signal == "move":
           # Assuming that the event.data contains a coordinate tuple.
           self.move (event.data)

