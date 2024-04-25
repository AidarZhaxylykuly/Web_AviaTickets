import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {AviaTour, Hotel, Reservation, Token, UnitUser, User, UserList} from "./models";
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TourService {

  BASE_URL = 'http://127.0.0.1:8000'

  constructor(private client: HttpClient) { }

  login(username: string, password: string): Observable<Token>{
    return this.client.post<Token>(
      `${this.BASE_URL}/api/login/`,
      {username, password}
    )
  }

  getUserList(): Observable<UserList>{
    return this.client.get<UserList>(`${this.BASE_URL}/api/login/list/`)
  }


  createUser(user: User): Observable<User>{
    return this.client.post<User>(
      `${this.BASE_URL}/api/login/create/`,
      {
        username: user.username,
        password: user.password,
        email: user.email
      }
    )
  }






  getTours(): Observable<AviaTour[]>{
    return this.client.get<AviaTour[]>(`${this.BASE_URL}/api/aviatours/`)
  }

  getTour(id: number): Observable<AviaTour>{
    return this.client.get<AviaTour>(`${this.BASE_URL}/api/aviatours/${id}`)
  }






  getHotels(): Observable<Hotel[]>{
    return this.client.get<Hotel[]>(`${this.BASE_URL}/api/hotels/`)
  }






  getReservations():Observable<Reservation[]>{
  return this.client.get<Reservation[]>(`${this.BASE_URL}/api/reservations/`)
  }

  createReservation(reservation: Reservation): Observable<Reservation>{
    return this.client.post<Reservation>(
      `${this.BASE_URL}/api/reservations/`,
      {
        user: reservation.user_id,
        unit_user: reservation.unit_user,
        num_of_people: reservation.num_of_people,
        acceptance: reservation.acceptance,
        hotel: reservation.hotel,
        aviatour: reservation.aviatour,
        total_cost: reservation.total_cost
      }
    )
  }

  createUnitUser(unit_user: UnitUser): Observable<UnitUser>{
    return  this.client.post<UnitUser>(
      `${this.BASE_URL}/api/users/`,
      {
        id: unit_user.id,
        user_id: unit_user.user_id,
        name: unit_user.name,
        surname: unit_user.surname,
        email: unit_user.email,
        contacts: unit_user.contacts
      }
    )
  }

  getUnitUser(id: number): Observable<UnitUser>{
    return this.client.get<UnitUser>(`${this.BASE_URL}/api/users/${id}`)
  }

  updateUnitUser(unit_user: UnitUser): Observable<UnitUser> {
    return this.client.put<UnitUser>(
      `${this.BASE_URL}/api/users/${unit_user.id}`,
      {
        id: unit_user.id,
        user_id: unit_user.user_id,
        name: unit_user.name,
        surname: unit_user.surname,
        email: unit_user.email,
        contacts: unit_user.contacts
      }
    )
  }
}
