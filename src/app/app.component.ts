import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {HeaderComponent} from "./header/header.component";
import { FooterComponent } from './footer/footer.component';
import { MainComponent } from './main/main.component';
import { SigninComponent } from './signin/signin.component';
import { AviamainComponent } from './aviamain/aviamain.component';
import { SignupComponent } from './signup/signup.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HeaderComponent, FooterComponent, MainComponent, SigninComponent, AviamainComponent, SignupComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'AviaTickets';
}
