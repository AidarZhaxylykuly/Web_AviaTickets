import {Component, OnInit} from '@angular/core';
import { FooterComponent } from '../footer/footer.component';
import {ActivatedRoute, RouterModule} from '@angular/router';
import {TourService} from "../tour.service";
import {Location} from "@angular/common";
import {Reservation, UnitUser, User, UserList} from "../models";
import {FormsModule} from "@angular/forms";

@Component({
  selector: 'app-signup',
  standalone: true,
  imports: [FooterComponent, RouterModule, FormsModule],
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.css'
})
export class SignupComponent implements OnInit{
  logged: boolean = false;
  userslist!: { id: number; username: string; }[];
  unit_user: UnitUser = {
    user_id: 0,
    name: '',
    surname: '',
    email: '',
    contacts: '',
  };
  user: User = {
    username: '',
    password: '',
    email: '',
  }

  name_pattern: RegExp = /^[A-Z][a-z]*$/;
  email_pattern: RegExp = /^[a-zA-Z0-9_]+@[a-z]+\.[a-z]{2,}$/;
  contact_pattern: RegExp = /^(?:\+?7|8)?\d{10}$/;

  constructor(private tourService: TourService, private location: Location){

  }

  ngOnInit(): void {
    const access = localStorage.getItem("access");
    if (access) {
      this.logged = true;
    }
  }

  getUserList(){
    this.tourService.getUserList().subscribe((user_list) => {
      this.userslist = user_list.users;
    })
  }

  login(){
    this.tourService.
    login(this.user.username, this.user.password).
    subscribe((data)=>{
      this.logged = true;
      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh);
    })
  }

  createUser0(): void {
    this.getUserList();
    this.user.email = this.unit_user.email;
    if (!this.userslist.find(user => user.username === this.user.username)) {
      this.tourService.createUser(this.user).subscribe((data) => {
          this.login();
      })
    } else {
      alert("This login is already exists");
    }
  }

  createUser(){
    // 1
    if(this.unit_user.name!=='' &&
      this.unit_user.surname!=='' &&
      this.unit_user.email!=='' &&
      this.unit_user.contacts!=='' &&
      this.user.username!=='' &&
      this.user.password!==''){
      if (!this.contact_pattern.test(this.unit_user.contacts)){
        alert("Invalid phone number");
        return;
      }
      if(!this.email_pattern.test(this.unit_user.email)){
        alert("Invalid email address");
        return;
      }
      if(!this.name_pattern.test(this.unit_user.name)){
        alert("Incorrect name");
        return;
      }
      if(!this.name_pattern.test(this.unit_user.surname)){
        alert("Incorrect surname");
        return;
      }
    }else{
      alert("Please, fill out all rows")
      return;
    }
    // 2
    this.createUser0()
    //3
    this.login()
    // 4
    const foundUser = this.userslist.find(user => user.username === this.user.username);
    this.unit_user.user_id = foundUser ? foundUser.id : 0;

    this.tourService
      .createUnitUser(this.unit_user)
      .subscribe((data) => {
      })
    // 5
    this.location.back();
  }
}
