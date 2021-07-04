import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { IStock } from '../interfaces/IStock';

@Injectable({
  providedIn: 'root',
})
export class StockService {
  private baseurl = environment.apiUrl + 'stock/';
  private getStockListUrl = this.baseurl + 'list';

  private trainModelUrl = this.baseurl + 'train';
  private splitImagesFromVideoUrl = this.baseurl + 'split-images';
  private uploadVideoUrl = this.baseurl + 'post';

  constructor(private http: HttpClient) {}

  public getStockList(): Observable<IStock[]> {
    return this.http.get<IStock[]>(this.getStockListUrl);
  }

  public trainModel(key): Observable<any> {
    return this.http.post<any>(this.trainModelUrl, { key: key });
  }
  public splitImagesFromVideo(): Observable<any> {
    return this.http.get<any>(this.splitImagesFromVideoUrl);
  }
  public uploadVideo(model): Observable<any> {
    return this.http.post<any>(this.uploadVideoUrl, model, {});
  }
}
