import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-meme-widget',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './meme-widget.component.html',
  styleUrls: ['./meme-widget.component.scss']
})
export class MemeWidgetComponent implements OnInit {
  @Input() data: string = '';
  @Output() onVote = new EventEmitter<{ widgetType: string, isPositive: boolean }>();

  hasVoted = false;
  currentMemeUrl: string = '';

  private readonly memeUrls: string[] = [
    'https://i.imgflip.com/5c7lwq.jpg',
    'https://i.imgflip.com/1ur9b0.jpg',
    'https://i.imgflip.com/4tztcw.jpg',
    'https://i.imgflip.com/2s3x2p.jpg',
    'https://i.imgflip.com/4i9q9o.jpg'
  ];

  ngOnInit(): void {
    this.selectRandomMeme();
  }

  selectRandomMeme(): void {
    const randomIndex = Math.floor(Math.random() * this.memeUrls.length);
    this.currentMemeUrl = this.memeUrls[randomIndex];
  }

  vote(isPositive: boolean) {
    if (this.hasVoted) return;
    this.hasVoted = true;
    this.onVote.emit({ widgetType: 'fun_meme', isPositive });
  }
}

