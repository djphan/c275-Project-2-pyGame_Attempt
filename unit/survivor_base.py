from unit.base_unit import BaseUnit
import unit, helperfunctions, maps, pygame

# Layer of the Survivor units for rendering
SURVIOR_LAYER = 3

class SurvivorUnit(BaseUnit):
    """
    This is the base zombie unit that all enemies are determined on.
    This class will contain all the necessary functions to run the zombie
    unit 
    """
    def __init__(self, **keywords):
        #load the base class
        super(SurviorUnit, self).__init__(**keywords)
        
        #All air units have the same movement sound
        self.move_sound = None

        #set unit specific things.
        self.type = "Survior"
        
    def activate(self):
        """
        Adds this unit to the active roster. Sets it to a higher layer so that
        it draws on top of other units.
        """
        super(SurviorUnit, self).activate()
        BaseUnit.active_units.change_layer(self, SURVIOR_LAYER)
        
    def is_stoppable(self, tile, pos):
        """
        Returns whether or not a unit can stop on a certain tile.
        """
        dist = helper.manhattan_dist((self.tile_x, self.tile_y), pos)
        
        # Check if this is too close to stop in
        if (dist < self.min_move_distance and
            (not self.is_docked(pos))):
            return False
            
        return super().is_stoppable(tile, pos)
        
    def get_defense(self, tile = None):
        """
        Returns this unit's defense.
        If a tile is specified the tile's defense bonus is added to
        the return value.
        
        Overrides the superclass method because planes are unaffected
        by terrain bonus defense.
        """
        return self.defense
        
    def can_turn_end(self):
        """
        Returns whether the player turn can end.
        """
        # We haven't moved, and we aren't docked, so we can't finish the turn
        if (not self.turn_state[0] and
            not self.is_docked(self.tile_pos)):
            return False
        
        # Default to the superclass
        return super().can_turn_end()
        
    def turn_ended(self):
        """
        Called when the turn is ended. Runs the aircraft out of fuel, or refuels
        if there's a carrier nearby.
        """
        super().turn_ended()
        
        # Refuel at carriers
        if self.is_docked(self.tile_pos):
            self.set_fuel(self.max_fuel)
            return True
        
        # Decrease fuel each turn
        self.set_fuel(self.fuel - 1)
        
        # Die if we're out of fuel
        if self.fuel <= 0:
            self.hurt(self.max_health)
            return False
            
        return True
        
    def is_passable(self, tile, pos):
        """
        Returns whether or not this unit can move over a certain tile.
        """
        # Return default
        if not super().is_passable(tile, pos):
            return False
            
        # We can't pass through enemy air units.
        u = BaseUnit.get_unit_at_pos(pos)
        if u and u.team != self.team and isinstance(u, AirUnit):
            return False

        # Air units can pass over everything else
        return True
        
    def is_tile_in_range(self, from_tile, from_pos, to_pos):
        """
        Checks to see if a tile is in attackable range from its current
        position. Takes tile range bonus into account.
        
        Overrides superclass method because planes are unaffected
        by terrain range bonus.
        """
        # Get range
        r = self.max_atk_range
        
        dist = helper.manhattan_dist(from_pos, to_pos)
        if dist <= r:
            return True
        return False


