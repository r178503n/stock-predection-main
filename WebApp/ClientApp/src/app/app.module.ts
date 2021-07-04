import { HttpClient, HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoadingBarHttpClientModule } from '@ngx-loading-bar/http-client';



//import * as firebase from 'firebase';
import { environment } from 'src/environments/environment';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ApplicationSharedModules } from './application-shared/modules/application-shared.module';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [

  
    BrowserModule,
    HttpClientModule,
    FormsModule,
    LoadingBarHttpClientModule,
    BrowserAnimationsModule,
    ApplicationSharedModules,
    AppRoutingModule,
  ],
  providers: [
    
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}