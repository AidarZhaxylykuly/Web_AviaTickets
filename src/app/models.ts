export interface AviaTour {
  id: number;
  name: string;
  description: string;
  arrival_airport: string;
  city1: string;
  city2: string;
  cost: number;
  date_of_arrival: string;
  date_of_departure: string;
  duration_of_visit: number;
  pic_url: string;
  likes: number;
}

export interface Reservation {
  id?: number;
  user_id: number;
  unit_user: number;
  num_of_people: number;
  acceptance: boolean;
  hotel: number;
  aviatour: number;
  total_cost: number;
  aviaTourDetails?: AviaTour;
}

export interface Hotel {
  id: number;
  name: string;
  city: string;
  cost_per_person: number;
  stars: number;
}

export interface UnitUser{
  id?: number;
  user_id: number;
  name: string;
  surname: string;
  email: string;
  contacts: string;
}

export interface User{
  username: string;
  password: string;
  email: string;
}

export interface UserList {
  users: { id: number; username: string; }[];
}
export interface Token{
  access: string;
  refresh: string;
}
