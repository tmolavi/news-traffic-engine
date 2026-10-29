"""
CLI Interface for News Traffic Engine.
Author: Taghi Molavi (https://molavi.pro)
Enterprise Partner: Inten (https://inten.asia)
"""

import click
import json
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from engine.geo.citability_analyzer import NewsCitabilityAnalyzer
from engine.indexing.google_indexing import GoogleIndexingClient
from engine.indexing.indexnow import IndexNowClient
from engine.indexing.sitemap_generator import GoogleNewsSitemapBuilder
from engine.schema.schema_builder import NewsSchemaBuilder
from engine.performance.discover_vitals_checker import GoogleDiscoverReadinessChecker
from engine.geo.llms_txt_builder import LlmsTxtBuilder
from engine.geo.robots_txt_generator import RobotsTxtGenerator

console = Console()


@click.group()
def cli():
    """News Traffic Engine: Autonomous AI Agent Framework for Newsroom Traffic, Google News & Discover Growth."""
    pass


@cli.command()
def info():
    """Display engine information, author, and enterprise partnership."""
    panel = Panel(
        "[bold cyan]News Traffic Engine[/bold cyan] v1.0.0\n"
        "[white]Autonomous AI Agent Framework for Newsroom Traffic & Generative Engine Optimization (GEO)[/white]\n\n"
        "[bold green]Author:[/bold green] Taghi Molavi ([link=https://molavi.pro]https://molavi.pro[/link])\n"
        "[bold magenta]Enterprise Partner:[/bold magenta] Inten ([link=https://inten.asia]https://inten.asia[/link])\n"
        "[bold yellow]License:[/bold yellow] MIT",
        title="⚡ News Traffic Engine",
        border_style="cyan",
    )
    console.print(panel)


@cli.command()
@click.option("--headline", required=True, help="News headline")
@click.option("--lead", required=True, help="Lead paragraph (first 40-60 words)")
@click.option("--body", required=True, help="Body text or path to body file")
def audit_geo(headline: str, lead: str, body: str):
    """Audit news copy for Citability in ChatGPT Search, Perplexity & AI Overviews."""
    # Check if body is a file path
    try:
        with open(body, "r", encoding="utf-8") as f:
            body_content = f.read()
    except Exception:
        body_content = body

    analyzer = NewsCitabilityAnalyzer()
    res = analyzer.analyze(headline=headline, lead_paragraph=lead, body_text=body_content)

    table = Table(title=f"GEO Citability Audit: {headline[:40]}...")
    table.add_column("Criterion", style="cyan")
    table.add_column("Score", style="bold green")

    for k, v in res["breakdown"].items():
        table.add_row(k.replace("_", " ").title(), str(v))

    table.add_row("[bold]Total Citability Score[/bold]", f"[bold yellow]{res['citability_score']}/100 ({res['grade']})[/bold yellow]")
    console.print(table)

    if res["recommendations"]:
        console.print("\n[bold red]Actionable GEO Recommendations:[/bold red]")
        for rec in res["recommendations"]:
            console.print(f"  • {rec}")


@cli.command()
@click.option("--url", required=True, help="Article URL to dispatch")
@click.option("--provider", default="google", type=click.Choice(["google", "indexnow"]), help="Indexing target")
def index_url(url: str, provider: str):
    """Dispatch URL to search engine indexing APIs for sub-15-minute inclusion."""
    if provider == "google":
        client = GoogleIndexingClient()
        res = client.publish_url_mock(url)
        console.print(f"[green]Google Indexing API payload simulated successfully for:[/green] {url}")
        console.print(res)
    else:
        client = IndexNowClient(host="example.com", key="sample-key")
        res = client.submit_mock([url])
        console.print(f"[green]IndexNow payload submitted successfully for:[/green] {url}")
        console.print(res)


@cli.command()
@click.option("--head-html", default="<meta name='robots' content='max-image-preview:large'>", help="HTML <head> content")
@click.option("--image-width", default=1200, type=int, help="Width in pixels of lead image")
@click.option("--image-height", default=675, type=int, help="Height in pixels of lead image")
def check_discover(head_html: str, image_width: int, image_height: int):
    """Check if article meets Google Discover eligibility criteria."""
    checker = GoogleDiscoverReadinessChecker()
    res = checker.evaluate_article(html_head=head_html, lead_image_width=image_width, lead_image_height=image_height)

    color = "green" if res["discover_readiness_score"] >= 80 else "yellow"
    console.print(f"[{color}]Discover Readiness Score: {res['discover_readiness_score']}/100 ({res['status']})[/{color}]")
    for check in res["passed_checks"]:
        console.print(f"  [green]✓[/green] {check}")
    for issue in res["issues"]:
        console.print(f"  [red]✗[/red] {issue}")


if __name__ == "__main__":
    cli()
