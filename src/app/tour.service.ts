import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {AviaTour, Hotel, Reservation, Token} from "./models";
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

  getTours(): Observable<AviaTour[]>{
    return this.client.get<AviaTour[]>(`${this.BASE_URL}/api/aviatours/`)
  }

  getHotels(): Observable<Hotel[]>{
    return this.client.get<Hotel[]>(`${this.BASE_URL}/api/hotels/`)
  }

  getTour(id: number): Observable<AviaTour>{
    return this.client.get<AviaTour>(`${this.BASE_URL}/api/aviatours/${id}`)
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
}
